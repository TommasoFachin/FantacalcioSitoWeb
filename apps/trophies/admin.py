from django.contrib import admin
from .models import Trophy

@admin.register(Trophy)
class TrophyAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'year')
    list_filter = ('title', 'year')