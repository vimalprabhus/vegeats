from datetime import datetime, date

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

from calc.models import Recipes

temp = ['qwerty','werty','ertyu']
@api_view(['POST','GET'])
def homeApi(request,**args):
    catogoryList = Recipes.objects.order_by().values_list('catogories', flat=True).distinct()
    if (request.GET.get('catogories',None) is None):
        recipes_list = list(Recipes.objects.all().values())
    else:
        recipes_list = list(Recipes.objects.filter(catogories = request.GET['catogories']).values())
    print(recipes_list[0]['Name'])



    return JsonResponse(recipes_list,safe=False)



def default(o):
    if isinstance(o, date):
        return o.isoformat()
    return o

