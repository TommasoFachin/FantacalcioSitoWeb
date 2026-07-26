from django.db import models
from django.conf import settings

class Trophy(models.Model):
    TROPHY_CHOICES = [
        ('Scudetto', 'Scudetto'),
        ('Coppa Italia', 'Coppa Italia'),
        ('Supercoppa', 'Supercoppa'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trophies')
    title = models.CharField(max_length=50, choices=TROPHY_CHOICES)
    year = models.CharField(max_length=9, help_text="Es: 2023/2024")

    def __str__(self):
        return f"{self.title} - {self.user.username} ({self.year})"