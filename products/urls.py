from django.urls import path
from . import views

urlpatterns = [
    path('see_products/', views.see_products, name='see_products'),
]