# Generated by Django 5.0.6 on 2025-01-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_useraccount_deposite'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='deposite',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True),
        ),
    ]
