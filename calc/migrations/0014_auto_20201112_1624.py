# Generated by Django 3.1.2 on 2020-11-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0013_recipes_catogories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='catogories',
            field=models.CharField(choices=[('starters', 'starters'), ('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner'), ('beverages', 'beverages')], default='others', max_length=200),
        ),
    ]
