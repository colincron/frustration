# Generated by Django 3.1.4 on 2021-01-04 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201216_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standarduser',
            name='pol_preference',
            field=models.CharField(choices=[('democratic_party', 'Democratic Party'), ('green_party', 'Green Party'), ('libertarian_party', 'Libertarian Party'), ('republican_party', 'Republican Party')], default='', max_length=30),
        ),
    ]