from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Payment
from .forms import PaymentForm

@login_required # Solo gli utenti loggati possono vedere il proprio bilancio
def payment_list(request):
    is_admin = request.user.is_staff

    # Calcola sempre il bilancio e i movimenti dell'utente loggato (admin incluso)
    my_payments = Payment.objects.filter(user=request.user).order_by('-date_added')
    
    debito_saldato = sum(p.amount for p in my_payments if p.is_paid and p.payment_type in ['Quota', 'Multa'])
    credito_saldato = sum(p.amount for p in my_payments if p.is_paid and p.payment_type == 'Premio')
    bilancio = credito_saldato - debito_saldato
    
    context = {
        'payments': my_payments,
        'bilancio': bilancio,
        'is_admin_view': is_admin,
    }

    if is_admin:
        # Se è admin, aggiungi al contesto i dati per la dashboard
        all_payments = Payment.objects.select_related('user').order_by('user__username', '-date_added')
        context['all_payments'] = all_payments

    return render(request, 'pagamenti.html', context)


def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin) # Solo gli admin possono aggiungere pagamenti
def payment_add(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pagamento aggiunto con successo!')
            return redirect('payments:list')
    else:
        form = PaymentForm()

    return render(request, 'payment_form.html', {'form': form})