# Generated by Django 2.2.13 on 2020-11-16 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20201113_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradinglog',
            name='buy_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tradinglog',
            name='sell_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tradinglog',
            name='stock_code',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='stockList',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.currentStock')),
            ],
        ),
    ]
