from django.test import TestCase
from django.utils.html import mark_safe
from datetime import date
from appli.models import Category, SizeStandard, SizeShoe, SizePant, Gender, Product
from django.core.files.uploadedfile import SimpleUploadedFile

class ModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title="Test Categorie")
        self.size_standard = SizeStandard.objects.create(title="Test Size Standard", display_order=1)
        self.size_shoe = SizeShoe.objects.create(title="Test Size Shoe")
        self.size_pant = SizePant.objects.create(title="Test Size Pant")
        self.gender = Gender.objects.create(title="Test Gender")
        # Create a mock image file
        self.image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )

        self.product = Product.objects.create(
            product_name="Test Product",
            product_price=10.00,
            product_category=self.category,
            product_gender=self.gender,
            product_description="Test product description",
            product_promotion_percentage=20,
            product_promotion_start_date=date(2023, 1, 1),
            product_promotion_end_date=date(2023, 12, 31),
            product_picture=self.image
        )

    def test_category_model(self):
        category = Category.objects.get(title="Test Categorie")
        self.assertEqual(str(category), "Test Categorie")

    def test_size_standard_model(self):
        size_standard = SizeStandard.objects.get(title="Test Size Standard")
        self.assertEqual(str(size_standard), "Test Size Standard")

    def test_size_shoe_model(self):
        size_shoe = SizeShoe.objects.get(title="Test Size Shoe")
        self.assertEqual(str(size_shoe), "Test Size Shoe")

    def test_size_pant_model(self):
        size_pant = SizePant.objects.get(title="Test Size Pant")
        self.assertEqual(str(size_pant), "Test Size Pant")

    def test_gender_model(self):
        gender = Gender.objects.get(title="Test Gender")
        self.assertEqual(str(gender), "Test Gender")

    def test_product_model(self):
        product = Product.objects.get(product_name="Test Product")
        self.assertEqual(str(product), "Test Product")
        self.assertEqual(product.image_tag(), mark_safe('<img src="%s" width="50" height="50"/>' % (product.product_picture.url)))
        self.assertEqual(product.is_discount(), True)
        discounted_price = product.product_price - product.product_price * product.product_promotion_percentage / 100
        self.assertEqual(product.promotion_price, discounted_price)
        # Test image_tag() method
        self.assertEqual(
            product.image_tag(),
            mark_safe('<img src="%s" width="50" height="50"/>' % (product.product_picture.url))
        )
        # test promotion detection method is_discount
        product.product_promotion_start_date = date(2023, 4, 19)
        product.product_promotion_end_date = date(2023, 4, 21)
        product.save()
        self.assertTrue(product.is_discount())
        product.product_promotion_start_date = date(2023, 4, 22)
        product.product_promotion_end_date = date(2023, 4, 23)
        product.save()
        self.assertFalse(product.is_discount())

        # Test promotion_price property calculation
        product.product_promotion_percentage = 50.00
        product.save()
        self.assertEqual(product.promotion_price, 5.00)