from django.contrib import admin
from django.db import models

Units = [('l','litre'), ('ml','milli Litre'), ('g','grams'), ('mg','milli Grams'), ('No','Nos.'), ('hf','Hand Full'), ('ts','Tea Spoon') ] #,'g' ,'mg', 'Nos', 'Hand ful', 'Tea Spoon' ]
catogories_list = [('starters','starters'),('breakfast','breakfast'),('lunch','lunch'),('dinner','dinner'),('beverages','beverages')]

class Recipes(models.Model):
    Name = models.CharField(max_length=200,primary_key=True)
    Date = models.DateField()
    Description = models.TextField()
    Brief = models.TextField(null=True,blank=True)
    IngrediantsPerson = models.IntegerField(default=1)
    Image = models.ImageField(upload_to='static/images/')
    catogories = models.CharField(max_length=200 , default='others', choices = catogories_list)


    def __str__(self):
        return self.Name

class Ingrediants_model(models.Model):
    id = models.AutoField(primary_key=True)
    IngridiantName = models.CharField(verbose_name='Ingrident',editable=True,max_length=200,null=True)
    Recipe = models.ForeignKey(Recipes,on_delete=models.CASCADE)
    IngridiantQty = models.DecimalField(verbose_name='Quantity',max_digits=5,decimal_places=2,null=True)
    IngridiantUnit = models.CharField(choices=Units,editable=True,max_length=20,null=True)
    OptionalTag = models.BooleanField(verbose_name='Optional',default=False)

    def __str__(self):
        return self.IngridiantName