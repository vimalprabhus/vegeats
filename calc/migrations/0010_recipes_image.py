# Generated by Django 3.1.2 on 2020-10-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0009_auto_20201023_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='Image',
            field=models.ImageField(default='test', upload_to='images/'),
            preserve_default=False,
        ),
    ]
