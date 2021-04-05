# Generated by Django 3.1.7 on 2021-04-05 20:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0015_remove_trip_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='my_trip',
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('CL', 'Clothings'), ('EL', 'Electronics'), ('EQ', 'Equipments'), ('PS', 'Personal'), ('MD', 'Medication'), ('OT', 'Others')], default='CL', max_length=2),
        ),
        migrations.AddField(
            model_name='trip',
            name='activity',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='country',
            field=models.CharField(default='Canada', max_length=50),
        ),
        migrations.AddField(
            model_name='trip',
            name='travelers',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='trip',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
