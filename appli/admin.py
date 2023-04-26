from django.contrib import admin
from .models import Product, Category, SizeStandard, SizeShoe, SizePant, Gender
from django.urls import reverse
from django.utils.html import format_html
from django import forms
# Register your models here.


admin.site.register(Category)

admin.site.register(Gender)


class MyModelAdminForm(forms.ModelForm):
    class Meta:
        exclude = ('product_promotion_percentage', 'product_promotion_start_date', 'product_promotion_end_date', 'product_promotion_price')  # Fields to exclude from the change form



#handle product display in admin
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','product_price','product_category','image_tag', 'discount')
    search_fields=('product_name__startswith',)

    form = MyModelAdminForm
    
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