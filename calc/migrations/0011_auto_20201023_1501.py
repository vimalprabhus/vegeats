# Generated by Django 3.1.2 on 2020-10-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0010_recipes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='Image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
