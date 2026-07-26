from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_type', 'amount', 'is_paid', 'date_added')
    list_filter = ('is_paid', 'payment_type', 'user')
    list_editable = ('is_paid',) # Permette all'admin di saldare con un click dalla lista
    search_fields = ('user__username', 'note')