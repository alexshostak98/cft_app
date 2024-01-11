from django.contrib import admin
from producer.models import Producer


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
