# Generated by Django 2.2.13 on 2020-11-17 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_currentstock_stock_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentstock',
            old_name='average_price',
            new_name='future_price',
        ),
        migrations.RemoveField(
            model_name='currentstock',
            name='earning_rate',
        ),
    ]
