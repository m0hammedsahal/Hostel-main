# Generated by Django 5.0.6 on 2025-02-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='fee_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='fee',
            name='fee_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fee',
            name='last_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
