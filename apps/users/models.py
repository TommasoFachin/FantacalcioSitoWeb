from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # I campi username, password, date_joined e last_login sono inclusi automaticamente in AbstractUser.
    # Manteniamo l'email per far sì che sia unica.
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'