from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='empty'),

    path('homepage', views.homepage, name='homepage'),
    path('catalogue', views.catalogue, name='catalogue'),
    path('catalogue/<str:gender>/', views.catalogue, name='pre_filtered_catalogue'),
    path('index', views.index, name= "index"),
    path('filter-data', views.filter_data, name='filter_data'),
    path('catalogue/<str:gender>/filter-data', views.filter_data, name='filter_data_from_prefiltered')

   

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)