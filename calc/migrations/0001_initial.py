# Generated by Django 3.1.2 on 2020-10-22 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('Name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('Date', models.DateField()),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediants_model',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('IngridiantName', models.CharField(max_length=200, null=True, verbose_name='Ingrident')),
                ('IngridiantQty', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Quantity')),
                ('IngridiantUnit', models.CharField(choices=[('l', 'litre'), ('ml', 'milli Litre'), ('g', 'grams'), ('mg', 'milli Grams'), ('No', 'Nos.'), ('hf', 'Hand Full'), ('ts', 'Tea Spoon')], max_length=20, null=True)),
                ('OptionalTag', models.BooleanField(default=False, verbose_name='Optional')),
                ('Recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='calc.recipes')),
            ],
        ),
    ]
