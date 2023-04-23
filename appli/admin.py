from django.contrib import admin
from .models import Product, Category, SizeStandard, SizeShoe, SizePant, Gender
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name', 'image_tag')


admin.site.register(Category)

admin.site.register(Gender)





class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','product_price','product_category','product_gender','image_tag')
    search_fields=('product_name__startswith',)
   
admin.site.register(Product, ProductAdmin)

class SizePantAdmin(admin.ModelAdmin):
    ordering=['title']

admin.site.register(SizePant, SizePantAdmin)

class SizeShoeAdmin(admin.ModelAdmin):
    ordering=['title']

admin.site.register(SizeShoe, SizeShoeAdmin)

class SizeStandardAdmin(admin.ModelAdmin):
    ordering=['display_order']

admin.site.register(SizeStandard, SizeStandardAdmin)