# Generated by Django 5.0.1 on 2024-01-11 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditapplication',
            name='number',
            field=models.IntegerField(unique=True),
        ),
    ]
