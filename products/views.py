from rest_framework import viewsets
from rest_framework import generics

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, ProductsByCategorySerializer


class ProductListView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ProductView(generics.RetrieveAPIView):
	lookup_field = 'slug'
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class CategoryListView(generics.ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class ProductsByCategoryListView(generics.ListAPIView):
	queryset = Category.objects.all()
	serializer_class = ProductsByCategorySerializer
