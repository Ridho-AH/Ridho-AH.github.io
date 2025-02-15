from django.urls import path
from django.urls import include, re_path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('product/', views.ProductView.as_view(), name='product'),
    path('product/<pk>/', views.ProductDetailView, name='product-detail'),
]