from .models import User, Customer, Product, Sale
from .serializers import UserSerializer, CustomerSerializer, ProductSerializer, SaleSerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse


class SitePermission(permissions.BasePermission):
    """
        Permission to check if a user has access to the site
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_trusted


class CustomerList(generics.ListCreateAPIView):
    """
        List all customers or create new Customer
    """
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer
    permission_classes = [SitePermission]


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, update or delete a customer instance
    """
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer
    permission_classes = [SitePermission]


class ProductList(generics.ListCreateAPIView):
    """
        List all products or create new product
    """
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [SitePermission]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, update or delete a product instance
    """
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [SitePermission]


class SaleList(generics.ListCreateAPIView):
    """
        List all sales or create new sale
    """
    queryset = Sale.objects.all().order_by('id')
    serializer_class = SaleSerializer
    permission_classes = [SitePermission]


class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, update or delete a sale instance
    """
    queryset = Sale.objects.all().order_by('id')
    serializer_class = SaleSerializer
    permission_classes = [SitePermission]


class AnalyticsList(APIView):
    """
        Provides analytics of the mall
    """
    
    def get(self, request):
        if not request.user.is_authenticated or not request.user.is_trusted:
            return Response(data={"detail":"Unauthorized user."}, status=status.HTTP_403_FORBIDDEN)
        
        thirty = timezone.now() - timezone.timedelta(days=30)
        sales = Sale.objects.filter(date_added__gte=thirty)
        employees = dict()
        products = dict()
        customers = dict()
        total_sale = 0
        
        for sale in sales:
            sale_price = sale.item.cost*sale.quantity
            total_sale += sale_price
            try:
                employees[sale.sold_by.username] += sale_price
            except KeyError:
                employees[sale.sold_by.username] = sale_price
            try:
                products[sale.item.item_name] += sale.quantity
            except KeyError:
                products[sale.item.item_name] = sale.quantity
            try:
                customers[sale.buyer.name] += sale_price
            except KeyError:
                customers[sale.buyer.name] = sale_price

        employees = sorted(employees.items(), reverse=True)
        products = sorted(products.items(), reverse=True)
        customers = sorted(customers.items(), reverse=True)

        data = {
            "max_sale_employees":employees,
            "max_sold_products":products,
            "high_val_customers":customers,
            "total_sale":total_sale
        }

        return Response(data=data)
    