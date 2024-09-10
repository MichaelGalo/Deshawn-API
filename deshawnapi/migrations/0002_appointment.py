# Generated by Django 5.1.1 on 2024-09-10 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deshawnapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('walker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='deshawnapi.walker')),
            ],
        ),
    ]
