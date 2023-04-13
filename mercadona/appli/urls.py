from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('homepage', views.homepage, name='homepage'),
    path('catalogue', views.catalogue, name='catalogue'),
    path('index', views.index, name= "index"),
    path('filter-data', views.filter_data, name='filter_data'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)