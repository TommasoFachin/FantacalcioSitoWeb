from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Payment

@login_required # Solo gli utenti loggati possono vedere il proprio bilancio
def payment_list(request):
    context = {}
    is_admin = request.user.is_staff

    if is_admin:
        # L'admin vede tutti i pagamenti, raggruppati per utente
        all_payments = Payment.objects.select_related('user').order_by('user__username', '-date_added')
        context['all_payments'] = all_payments
        context['is_admin_view'] = True
    else:
        # L'utente normale vede solo i suoi pagamenti e il suo bilancio
        my_payments = Payment.objects.filter(user=request.user).order_by('-date_added')
        
        # Logica per il calcolo del bilancio basata sui movimenti SALDATI
        debito_saldato = sum(p.amount for p in my_payments if p.is_paid and p.payment_type in ['Quota', 'Multa'])
        credito_saldato = sum(p.amount for p in my_payments if p.is_paid and p.payment_type == 'Premio')
        bilancio = credito_saldato - debito_saldato
        
        context['payments'] = my_payments
        context['bilancio'] = bilancio

    return render(request, 'pagamenti.html', context)