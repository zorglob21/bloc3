from django.test import SimpleTestCase

from django.urls import reverse, resolve
from .. import views

class TestUrls(SimpleTestCase):
    
    def test_index_url_is_resolved(self):
        url= reverse('index')
        self.assertEquals(resolve(url).func, views.index)
    
    def test_catalogue_url_is_resolved(self):
        url= reverse('catalogue')
        self.assertEquals(resolve(url).func, views.catalogue)

    def test_filter_data_url_is_resolved(self):
        url= reverse('filter_data')
        self.assertEquals(resolve(url).func, views.filter_data)
    
    def test_empty_url_is_resolved(self):
        url= reverse('empty')
        self.assertEquals(resolve(url).func, views.index )