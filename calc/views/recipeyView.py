from django.shortcuts import render
from calc.models import Recipes, Ingrediants_model


def recipyview(request,recipes_name):

    catogoryList =Recipes.objects.order_by().values_list('catogories', flat=True).distinct()
    recipes_name = recipes_name.lower()
    print(recipes_name)
    IngrediantsData = Ingrediants_model.objects.filter(Recipe = recipes_name)
    RecipesData = Recipes.objects.get(Name = recipes_name)
    return render(request, 'calc/recipy.html', context={'Ingrediants': IngrediantsData,'Recipy':RecipesData ,  'catogoryList':catogoryList})
