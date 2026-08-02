from django import forms
from django.contrib.auth import get_user_model
from .models import Payment

User = get_user_model()

class PaymentForm(forms.ModelForm):
    # Filtriamo gli utenti per mostrare solo i partecipanti normali, non lo staff/admin
    user = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=False, is_superuser=False).order_by('username'),
        label="Utente",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['payment_type'].widget.attrs.update({'class': 'form-select'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Es. 5.00'})
        self.fields['note'].widget.attrs.update({'class': 'form-control', 'rows': 3})
        self.fields['is_paid'].widget.attrs.update({'class': 'form-check-input'})

        # Aggiungiamo un tocco in più per l'importo, specificando che è un numero
        self.fields['amount'].widget.input_type = 'number'
        self.fields['amount'].widget.attrs['step'] = '0.01'

    class Meta:
        model = Payment
        fields = ['user', 'payment_type', 'amount', 'note', 'is_paid']
        labels = {
            'payment_type': 'Tipo di Pagamento',
            'amount': 'Importo (€)',
            'note': 'Note (es. "Multa per formazione non inviata")',
            'is_paid': 'Il movimento è già stato saldato?',
        }