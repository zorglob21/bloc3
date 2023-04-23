from django.test import TestCase, Client
from django.urls import reverse
from appli.models import *
import inspect
from django.http import JsonResponse
from django.template.loader import render_to_string

class TestViews(TestCase):
    
    def create(self, title="only a test", body="yes, this is only a test"):
        return Category.objects.create(title=title, body=body)
    
    def test_view_index(self):
        w = self.create()
        client = Client()
        response = client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(w.title, response.content)
    
    def test_view_homepage(self):
        client = Client()
        response = client.get(reverse('homepage'))
        self.assertEquals(response.status_code, 200)

    def test_view_index(self):
        client = Client()
        response = client.get(reverse('catalogue'))
        self.assertEquals(response.status_code, 200)
 


class FilterDataViewTest(TestCase):
    def setUp(self):
        # Set up any necessary data for the test
        self.url = reverse('filter_data')  

    def test_filter_data_view_returns_json_response(self):
        # Issue a GET request to the view
        response = self.client.get(self.url)

        # Assert that the response is a JsonResponse
        self.assertIsInstance(response, JsonResponse)

    def test_filter_data_view_returns_expected_data(self):
        # Set up query parameters for the request
        params = {
         
            'maxPrice': "100.00",
            'categorie_list["homme"]': [],
            'gender_list[]': [],
            'size_standard[]': [],
            'size_pants["32"]': [],
            'size_shoes[]': [],
               
        }

        # Issue a GET request to the view with query parameters
        response = self.client.get(self.url, params)

        # Assert that the response contains the expected data
        max_price = float(params['maxPrice'])
        expected_queryset = Product.objects.filter(product_price__lte=max_price)
    
        # Render the expected queryset to a string
        expected_data = {'data': render_to_string('appli/ajax-product-list.html', {'data': expected_queryset})}

        # Assert that the response contains the expected data
        self.assertDictEqual(response.json(), expected_data)
