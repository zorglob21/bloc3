from django.shortcuts import render
from .forms import FilterForm
from django.http import HttpResponse
from django.template import loader
from .models import Product

def index(request):
    template = loader.get_template('appli/index.html')
    context = {}
    return HttpResponse(template.render(context,request))

def homepage(request):
    template = loader.get_template('appli/homepage.html')
    context = {}
    return HttpResponse(template.render(context,request))

def catalogue(request):
    data = Product.objects.all().order_by('product_name')
    template = loader.get_template('appli/catalogue.html')
    context = {"data": data}
    return HttpResponse(template.render(context,request))

