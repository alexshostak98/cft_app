# Generated by Django 5.0.1 on 2024-01-11 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_application', '0002_alter_creditapplication_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditapplication',
            name='number',
            field=models.BigIntegerField(unique=True),
        ),
    ]
