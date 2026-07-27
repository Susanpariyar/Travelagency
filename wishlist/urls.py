from django.urls import path
from . import views

urlpatterns = [
    path('add/<slug:slug>/',views.add_to_wishlist, name='add_to_wishlist'),

    path('remove/<slug:slug>/', views.remove_from_wishlist, name='remove_from_wishlist' ),

    path( '',views.my_wishlist, name='my_wishlist' ),

    path('toggle/<slug:slug>/', views.toggle_wishlist, name='toggle_wishlist' ),

    
]