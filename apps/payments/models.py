from django.db import models
from django.conf import settings
from django.core.mail import send_mail

class Payment(models.Model):
    TYPE_CHOICES = [
        ('Quota', 'Quota di Iscrizione'),
        ('Multa', 'Multa'),
        ('Premio', 'Premio'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    payment_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    note = models.TextField(blank=True, null=True, help_text="Aggiungi una nota (Es. 'Dimenticanza formazioni')")
    is_paid = models.BooleanField(default=False, help_text="Spunta questa casella quando il partecipante ha pagato o ha ricevuto il premio")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.payment_type} - {self.user.username} - €{self.amount} ({'Saldato' if self.is_paid else 'Pendente'})"

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        # Invia email all'utente se gli viene assegnata una multa o un premio
        if is_new and self.payment_type in ['Multa', 'Premio'] and self.user.email:
            try:
                send_mail(f"Nuovo {self.payment_type} FANTALEGA VsC", f"Ciao {self.user.username},\n\nL'admin ti ha assegnato un {self.payment_type} di {self.amount}€.\nNota: {self.note or 'Nessuna nota specificata'}.", 'admin@fantalega.vsc', [self.user.email], fail_silently=True)
            except Exception:
                pass # Ignoriamo l'errore se il server SMTP non è configurato