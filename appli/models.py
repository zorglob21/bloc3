from django.db import models
from django.utils.html import mark_safe
from datetime import date
from decimal import Decimal
from django.conf import settings
from cloudinary.models import CloudinaryField

class Category(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title
    
class SizeStandard(models.Model):
    title = models.CharField(max_length=50)
    display_order = models.SmallIntegerField()
    
    def __str__(self):
        return self.title

class SizeShoe(models.Model):
    title = models.CharField(max_length=50)
   
    
    def __str__(self):
        return self.title

class SizePant(models.Model):
    title = models.CharField(max_length=50)


    def __str__(self):
        return self.title

class Gender(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Product(models.Model):
    product_name =models.CharField(max_length=70)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_gender = models.ForeignKey(Gender, on_delete=models.CASCADE, default='')
    product_size_standard = models.ManyToManyField(SizeStandard, blank=True)
    product_size_pants = models.ManyToManyField(SizePant, blank=True)
    product_size_shoes = models.ManyToManyField(SizeShoe, blank=True)
    product_description = models.TextField(blank=True)
    product_promotion_percentage=models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    product_promotion_start_date=models.DateField(blank=True,null=True)
    product_promotion_end_date=models.DateField(blank=True,null=True)
   
    
    if settings.DEBUG == True:
        product_picture=models.ImageField(upload_to='images/')
    
    elif settings.DEBUG == False:
        product_picture=CloudinaryField('image')
    
    def __str__(self):
        return self.product_name

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50"/>'%(self.product_picture.url))
    
    
    def is_discount(self):
        "returns if the item is on promotion and the promotion price"
        today = date.today()
        if self.product_promotion_start_date < today and self.product_promotion_end_date > today:
            return True
        else:
            return False
    
    
    
    @property
    def promotion_price(self):
        discounted_price = self.product_price - self.product_price* (Decimal(str(self.product_promotion_percentage))/100)
        return discounted_price

 