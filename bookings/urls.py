from django.urls import path
from . import views


urlpatterns = [

    path("book/<slug:slug>/",views.book_package,name="book_package"),
    path("my-bookings/",views.my_bookings,name="my_bookings"),
    path("details/<str:booking_id>/",views.booking_detail,name="booking_detail"),
    path("cancel/<str:booking_id>/",views.cancel_booking,name="cancel_booking"),

]