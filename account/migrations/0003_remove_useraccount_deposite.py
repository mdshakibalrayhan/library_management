# Generated by Django 5.0.6 on 2025-01-20 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_useraccount_deposite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='deposite',
        ),
    ]
