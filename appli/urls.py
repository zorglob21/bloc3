from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='empty'),
    path('catalogue', views.catalogue, name='catalogue'),
    #to be used for creating pre-filtered links for the catalogue
    path('catalogue/<str:gender>/', views.catalogue, name='pre_filtered_catalogue'),
    path('index', views.index, name= "index"),
    path('filter-data', views.filter_data, name='filter_data'),
    #necessary additional url for the filter to work correctly if you access the catalogue via prefiltered url links
    path('catalogue/<str:gender>/filter-data', views.filter_data, name='filter_data_from_prefiltered'),
    path('product/<int:product_id>/edit_promotion/', views.edit_promotion, name='edit_promotion')
   

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)