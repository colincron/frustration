# Generated by Django 3.1.5 on 2021-01-28 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standarduser',
            name='politician_list',
        ),
    ]
