from django.http import HttpResponse
from django.shortcuts import render

from calc.models import Recipes

temp = ['qwerty','werty','ertyu']
def home(request,**args):

    catogoryList = Recipes.objects.order_by().values_list('catogories', flat=True).distinct()
    if (request.GET.get('catogories',None) is None):
        recipes_list = list(Recipes.objects.all().values())
    else:
        recipes_list = list(Recipes.objects.filter(catogories = request.GET['catogories']).values())
    return render(request,'calc/index.html',context={'data':recipes_list , 'catogoryList':catogoryList})
# Create your views here.
