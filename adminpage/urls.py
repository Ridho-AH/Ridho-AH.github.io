from django.urls import path
from django.urls import include, re_path
from . import views

urlpatterns = [
    path('', views.StockListView.as_view(), name='stock'),
    path('new', views.StockCreateView, name='new-stock'),
    path('stock/<pk>/edit', views.StockEditView, name='edit-stock'),
    path('stock/<pk>/delete', views.StockDeleteView.as_view(), name='delete-stock'),
    path('guide/', views.GuideView.as_view(), name='guide')
]