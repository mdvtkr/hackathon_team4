# Generated by Django 2.2.13 on 2020-11-16 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20201116_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentstock',
            name='previous_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]