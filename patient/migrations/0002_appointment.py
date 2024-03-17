# Generated by Django 5.0.2 on 2024-03-08 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, null=True)),
                ('date', models.DateField(max_length=50, null=True)),
                ('time', models.TimeField(max_length=50, null=True)),
                ('message', models.TextField(max_length=500, null=True)),
                ('status', models.TextField(max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
            ],
        ),
    ]
