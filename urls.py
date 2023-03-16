from django.urls import path

from . import views

urlpatterns = [
    path('customer/', views.customer),
    path('sellers/', views.seller),
    path('forms/', views.add_seller),
    path('forms2/', views.add_customer),
]