# Generated by Django 3.1.2 on 2020-10-23 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0007_ingrediants_model_ingrediantsperson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediants_model',
            name='IngrediantsPerson',
            field=models.IntegerField(default=1),
        ),
    ]