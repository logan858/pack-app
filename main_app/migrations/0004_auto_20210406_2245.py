# Generated by Django 3.1.7 on 2021-04-07 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_auto_20210406_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
        migrations.RemoveField(
            model_name='item',
            name='vote',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='travelers',
        ),
        migrations.AddField(
            model_name='trip',
            name='number_items',
            field=models.IntegerField(default=15),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('vote', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]