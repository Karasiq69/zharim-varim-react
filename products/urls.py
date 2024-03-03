from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ProductsByCategoryListView

app_name = 'products'

router = DefaultRouter()

router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('products-by-category/', ProductsByCategoryListView.as_view(), name='products-by-category'),

]
