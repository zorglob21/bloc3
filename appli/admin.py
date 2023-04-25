from django.contrib import admin
from .models import Product, Category, SizeStandard, SizeShoe, SizePant, Gender
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.


admin.site.register(Category)

admin.site.register(Gender)




#handle product display in admin
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','product_price','product_category','image_tag', 'discount')
    search_fields=('product_name__startswith',)
    fieldsets = (
        (None, {
            'fields': ('product_name','product_price','product_category','product_gender','product_size_standard'
            ,'product_size_pants','product_size_shoes','product_description','product_picture')
        }),
        ('Informations de promotion', {
            'classes': ('collapse',),
            'fields': ('product_promotion_percentage', 'product_promotion_start_date', 'product_promotion_end_date'),
        }),
    )

    
    def discount(self, obj):
        # Generate the URL for the "change" view of the Product model for the specific object
        url = reverse('edit_promotion', args=[obj.id])
        # Return a formatted HTML link with a button-like appearance
        return format_html('<a class="button" href="{}">Promotion</a>', url)
   
admin.site.register(Product, ProductAdmin)

#to display sub fields in ordered manner when adding a new entry on Product
class SizePantAdmin(admin.ModelAdmin):
    ordering=['title']

admin.site.register(SizePant, SizePantAdmin)

class SizeShoeAdmin(admin.ModelAdmin):
    ordering=['title']

admin.site.register(SizeShoe, SizeShoeAdmin)

class SizeStandardAdmin(admin.ModelAdmin):
    ordering=['display_order']

admin.site.register(SizeStandard, SizeStandardAdmin)