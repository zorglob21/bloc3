from django.db import models
from django.utils.html import mark_safe
from datetime import date
# Create your models here.

#class Admin(models.Model):
   #admin_pseudo = models.CharField(max_length=50)
   #admin_password = models.CharField(max_length=250)
#ajuster le max length à la longueur du hash


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
    #product_promotion_price=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_promotion_start_date=models.DateField(blank=True,null=True)
    product_promotion_end_date=models.DateField(blank=True,null=True)
    product_picture=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.product_name

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50"/>'%(self.product_picture.url))
    
    #def discount_link(self, obj):
        #url = "admin:%(appli)s_%(model)s_%(page)"
        #return format_html('<a href="{}">{}xxx</a>')
    
    def is_discount(self):
        "returns if the item is on promotion and the promotion price"
        today = date.today()
        if self.product_promotion_start_date < today and self.product_promotion_end_date > today:
            return True
        else:
            return False
    
    
    
    @property
    def promotion_price(self):
        discounted_price = self.product_price - self.product_price*self.product_promotion_percentage/100
        return discounted_price
        