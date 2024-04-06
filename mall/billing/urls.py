from django.urls import path
from . import views

# format_suffix_patterns is commented to reduce the endpoints for the API

# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('customers/', views.CustomerList.as_view()),
    path('customers/<int:pk>/', views.CustomerDetail.as_view()),
    path('sales/', views.SaleList.as_view()),
    path('sales/<int:pk>/', views.SaleDetail.as_view()),
    path('analytics/', views.AnalyticsList.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)