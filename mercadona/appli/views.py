from django.shortcuts import render
from .forms import FilterForm
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import *
from django.template.loader import render_to_string

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
    size_standard = SizeStandard.objects.all().order_by('display_order')
    size_pants = SizePant.objects.all().order_by('title')
    size_shoes = SizeShoe.objects.all().order_by('title')
    template = loader.get_template('appli/catalogue.html')
    context = {"data": data, "size_standard": size_standard, "size_pants": size_pants, "size_shoes" : size_shoes }
    return HttpResponse(template.render(context,request))

def filter_data(request):
    size_standard=request.GET.getlist('size_standard[]')
    size_pants=request.GET.getlist('size_pants[]')
    size_shoes=request.GET.getlist('size_shoes[]')
    allProducts= Product.objects.all().order_by('-id').distinct()
    if len(size_standard)>0 or len(size_pants)>0 or len(size_shoes)>0 :
       allProducts=allProducts.filter(product_size_standard__title__in = size_standard).distinct() | allProducts.filter(product_size_pants__title__in = size_pants).distinct() | allProducts.filter(product_size_shoes__title__in = size_shoes).distinct()
            
    t=render_to_string('appli/ajax-product-list.html', {'data':allProducts})
    return JsonResponse({'data': t})