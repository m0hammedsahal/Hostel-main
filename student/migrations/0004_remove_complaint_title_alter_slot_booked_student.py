# Generated by Django 5.0.6 on 2025-02-10 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_complaint_slot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='title',
        ),
        migrations.AlterField(
            model_name='slot',
            name='booked_student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]
