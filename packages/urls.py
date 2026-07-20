from django.urls import path
from . import views

urlpatterns = [
    path('', views.package_list, name='package_list'),
    path('destination/<slug:slug>/', views.destination_packages, name='destination_packages'),
    path('<slug:slug>/', views.package_detail, name='package_detail'),
]