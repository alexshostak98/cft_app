from django.contrib import admin
from credit_application.models import CreditApplication


@admin.register(CreditApplication)
class CreditApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'number',
    )
