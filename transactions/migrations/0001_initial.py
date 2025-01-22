# Generated by Django 5.0.6 on 2025-01-20 19:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0004_useraccount_deposite'),
        ('books', '0003_alter_allbooks_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTranscations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('BORRWING', 'BORROWING'), ('RETURNING', 'RETURNING')], max_length=15)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.allbooks')),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.useraccount')),
            ],
        ),
    ]
