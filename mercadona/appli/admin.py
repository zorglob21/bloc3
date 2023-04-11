from django.contrib import admin
from .models import Product, Category, Size, Gender
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Gender)

#class ProductAdmin(admin.ModelAdmin):
    #list_display =('id', 'category','title', 'Price')
#admin.site.register(Product, ProductAdmin)