from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service_home_cleaning/', views.service_home_cleaning, name='service_home_cleaning'),
    path('book/availability/', views.booking_availability, name='booking_availability'),
    path('book/property-details/', views.property_details, name='property_details'),
    path('book/client-payment/', views.client_payment, name='client_payment'),
    path('book/confirm/', views.booking_confirm, name='booking_confirm'),

]