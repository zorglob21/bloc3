from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import *
from django.template.loader import render_to_string
from django.db.models import Max, Min
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    template = loader.get_template('appli/index.html')
    context = {}
    return HttpResponse(template.render(context,request))

def homepage(request):
    template = loader.get_template('appli/homepage.html')
    context = {}
    return HttpResponse(template.render(context,request))

def catalogue(request, gender=''):
    if gender == '':
        data = Product.objects.all().order_by('product_name')
    elif gender =="homme":
        data = Product.objects.all().order_by('product_name')
        data = data.filter(product_gender__title = 'homme') 
    elif gender =="femme":
        data = Product.objects.all().order_by('product_name')
        data = data.filter(product_gender__title = 'femme') 
    elif gender =="enfant":
        data = Product.objects.all().order_by('product_name')
        data = data.filter(product_gender__title = 'enfant')

    size_standard = SizeStandard.objects.all().order_by('display_order')
    size_pants = SizePant.objects.all().order_by('title')
    size_shoes = SizeShoe.objects.all().order_by('title')
    gender_list = Gender.objects.all().order_by('title')
   

    categorie_list = Category.objects.all().order_by('title')
    minMaxPrice = data.aggregate(Min('product_price'),Max('product_price'))
    template = loader.get_template('appli/catalogue.html')
    context = {"data": data, "size_standard": size_standard, "size_pants": size_pants, "size_shoes" : size_shoes,
    "gender_list":gender_list, 'categorie_list':categorie_list, "minMaxPrice":minMaxPrice}
    return HttpResponse(template.render(context,request))

def filter_data(request, gender =''):
    if gender == '':
        gender_list=request.GET.getlist('gender_list[]')   
    else:
        gender_list=[gender]     
    size_standard=request.GET.getlist('size_standard[]')
    size_pants=request.GET.getlist('size_pants[]')
    size_shoes=request.GET.getlist('size_shoes[]')
    categorie_list=request.GET.getlist('categorie_list[]')
    

    maxPrice=request.GET.get('maxPrice', '0.00')
    #maxPrice=request.GET['maxPrice']
    allProducts=Product.objects.all().order_by('-id').distinct()

    allProducts=allProducts.filter(product_price__lte=maxPrice)
    if len(size_standard)>0 or len(size_pants)>0 or len(size_shoes)>0:
       allProducts=allProducts.filter(product_size_standard__title__in = size_standard).distinct() | allProducts.filter(product_size_pants__title__in = size_pants).distinct() | allProducts.filter(product_size_shoes__title__in = size_shoes).distinct()
    if len(categorie_list)>0:
        allProducts = allProducts.filter(product_category__title__in = categorie_list).distinct()
    if len(gender_list)>0:
        allProducts=allProducts.filter(product_gender__title__in = gender_list).distinct()
                    
    
    context ={'data':allProducts}        
    t=render_to_string('appli/ajax-product-list.html', context)
    return JsonResponse({'data': t})





