from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name':'Wanderson'
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name':'Wanderson'
    })



# Create your views here.
