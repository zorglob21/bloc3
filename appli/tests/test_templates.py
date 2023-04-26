from django.test import TestCase
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render
from decimal import Decimal
from appli.models import *
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date
import json

class TemplateTests(TestCase):
    def test_product_list_template(self):
      # Create some dummy data for the test
      self.category = Category.objects.create(title="Test Categorie")
      self.size_standard = SizeStandard.objects.create(title="Test Size Standard", display_order=1)
      self.size_shoe = SizeShoe.objects.create(title="Test Size Shoe")
      self.size_pant = SizePant.objects.create(title="Test Size Pant")
      self.gender = Gender.objects.create(title="Test Gender")
      self.image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )

      product1 = Product.objects.create(
            product_name="Product1",
            product_price=Decimal('10.00'),
            product_category=self.category,
            product_gender=self.gender,
            product_description="Test product description",
            product_promotion_percentage=20,
            product_promotion_start_date=date(2022, 1, 1),
            product_promotion_end_date=date(2022, 12, 31),
            product_picture=self.image
        )


      product2 =  Product.objects.create(
            product_name="Product2",
            product_price=Decimal('100.00'),
            product_category=self.category,
            product_gender=self.gender,
            product_description="Test product description second product",
            product_promotion_percentage=30,
            product_promotion_start_date=date(2023, 1, 1),
            product_promotion_end_date=date(2033, 12, 31),
            product_picture=self.image
            
        )
      product2.product_promotion_price= product2.product_price - product2.product_price* (Decimal(str(product2.product_promotion_percentage))/100)
      # Save the mock Product objects to the database
      product1.save()
      product2.save()
      
      # Render the product list template

      url = reverse('filter_data')
      response = self.client.get(url, {
            'maxPrice': '10000',
            'size_standard[]': [],
            'categorie_list[]': [],
            'gender_list[]': []
        })
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'appli/ajax-product-list.html')

      # Check if the rendered JSON response contains the product names
      json_response = json.loads(response.content)
      self.assertIn('data', json_response)
      data_str = json_response['data']
    
      #print(json_response) to help debugging
  

      # Check that the filtered products are passed to the context
      filtered_products = response.context['data']
      self.assertEqual(filtered_products.count(), 2)
      self.assertEqual(filtered_products.first(), product2)

      # Check that the rendered HTML contains the filtered product's information
    
      self.assertContains(response, product1.product_name)
      self.assertContains(response, product1.product_price)
      self.assertContains(response, product1.product_picture.url)

      #check that the promotion price is calculated and displayed
      self.assertContains(response, round(product2.product_promotion_price, 2))
 