# Generated by Django 5.0.6 on 2025-02-10 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_alter_fee_fee_amount_alter_fee_fee_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fee',
            options={'ordering': ['id'], 'verbose_name': 'fee', 'verbose_name_plural': 'fees'},
        ),
        migrations.AlterModelTable(
            name='fee',
            table='faculty_fee',
        ),
    ]
