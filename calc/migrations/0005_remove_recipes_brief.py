# Generated by Django 3.1.2 on 2020-10-23 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_auto_20201023_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='Brief',
        ),
    ]