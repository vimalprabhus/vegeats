# Generated by Django 3.1.2 on 2020-10-23 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_recipes_brief'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='Brief',
            field=models.TextField(null=True),
        ),
    ]