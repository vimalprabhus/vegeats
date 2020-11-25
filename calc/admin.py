from django.contrib import admin


from calc.models import Recipes, Ingrediants_model

class IngrediantsInline(admin.TabularInline):
    model = Ingrediants_model

@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    inlines = [IngrediantsInline]

