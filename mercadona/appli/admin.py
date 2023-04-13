from django.contrib import admin
from .models import Product, Category, SizeStandard, SizeShoe, SizePant, Gender
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SizeStandard)
admin.site.register(Gender)
admin.site.register(SizeShoe)
admin.site.register(SizePant)
#class ProductAdmin(admin.ModelAdmin):
    #list_display =('id', 'category','title', 'Price')
#admin.site.register(Product, ProductAdmin)