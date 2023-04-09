from django.db import models

# Create your models here.

#class Admin(models.Model):
   #admin_pseudo = models.CharField(max_length=50)
   #admin_password = models.CharField(max_length=250)
#ajuster le max length à la longueur du hash

class Product(models.Model):
    product_name =models.CharField(max_length=70)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.CharField(max_length=70)
    product_gender = models.CharField(max_length=20)
    product_promoted=models.BooleanField(default=False)
    product_promotion_percentage=models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    product_promotion_price=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_promotion_end_date=models.DateField(blank=True,null=True)
    product_picture=models.ImageField(upload_to='uploads/%Y/%m/%d/')