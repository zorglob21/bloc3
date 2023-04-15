from django.shortcuts import render
from .forms import FilterForm
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

def catalogue(request):
    data = Product.objects.all().order_by('product_name')
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

def filter_data(request):
    size_standard=request.GET.getlist('size_standard[]')
    size_pants=request.GET.getlist('size_pants[]')
    size_shoes=request.GET.getlist('size_shoes[]')
    categorie_list=request.GET.getlist('categorie_list[]')
    gender_list=request.GET.getlist('gender_list[]')

    maxPrice=request.GET['maxPrice']
    
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



class ViewPaginatorMixin(object):
    min_limit = 1
    max_limit = 10

    def paginate(self, object_list, page=1, limit=10, **kwargs):
        try:
            page = int(page)
            if page < 1:
                page = 1
        except (TypeError, ValueError):
            page = 1

        try:
            limit = int(limit)
            if limit < self.min_limit:
                limit = self.min_limit
            if limit > self.max_limit:
                limit = self.max_limit
        except (ValueError, TypeError):
            limit = self.max_limit

        paginator = Paginator(object_list, limit)
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)
        data = {
            'previous_page': objects.has_previous() and objects.previous_page_number() or None,
            'next_page': objects.has_next() and objects.next_page_number() or None,
            'data': list(objects)
        }
        return data
