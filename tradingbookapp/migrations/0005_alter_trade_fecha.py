# Generated by Django 4.0.5 on 2022-06-28 12:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tradingbookapp', '0004_mercados_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='fecha',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 6, 28, 12, 53, 15, 660101, tzinfo=utc), verbose_name='Fecha de operacion (mm/dd/yyyy)'),
            preserve_default=False,
        ),
    ]
