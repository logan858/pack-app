# Generated by Django 3.1.7 on 2021-04-04 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_item_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
    ]
