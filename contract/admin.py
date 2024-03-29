from django.contrib import admin
from contract.models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'number',
        'credit_application',
    )
