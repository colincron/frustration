# Generated by Django 3.1.5 on 2021-01-28 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('politics', '0006_auto_20210127_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='constituent',
            field=models.CharField(max_length=50),
        ),
    ]