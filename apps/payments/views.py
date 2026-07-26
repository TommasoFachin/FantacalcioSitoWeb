from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Payment

@login_required # Solo gli utenti loggati possono vedere il proprio bilancio
def payment_list(request):
    # Filtriamo i pagamenti per mostrare solo quelli dell'utente connesso
    my_payments = Payment.objects.filter(user=request.user).order_by('-date_added')
    
    # Logica per il calcolo del bilancio
    debito = sum(p.amount for p in my_payments if not p.is_paid and p.payment_type in ['Quota', 'Multa'])
    credito = sum(p.amount for p in my_payments if not p.is_paid and p.payment_type == 'Premio')
    bilancio = credito - debito

    return render(request, 'pagamenti.html', {'payments': my_payments, 'bilancio': bilancio})