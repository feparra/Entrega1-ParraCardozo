# Generated by Django 4.0.5 on 2022-06-28 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradingbookapp', '0007_alter_notes_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mercado', models.CharField(max_length=250, verbose_name='mercado a donde pertenece')),
                ('simbolo', models.CharField(max_length=30, verbose_name='Simbolo')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha de operacion (mm/dd/yyyy)')),
                ('simbolo', models.CharField(max_length=30, verbose_name='Simbolo')),
                ('nota', models.CharField(max_length=250, verbose_name='Notas de trading')),
            ],
        ),
        migrations.DeleteModel(
            name='Mercados',
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
    ]
