from django.contrib import admin

# Register your models here.

from mptt.admin import MPTTModelAdmin

from .models import (
	Category,
	Product,
	ProductImage,
	ProductSpecification,
	ProductSpecificationValue,
	ProductType
)

admin.site.register(Category, MPTTModelAdmin)


class ProductSpecificationsInline(admin.TabularInline):
	model = ProductSpecification


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
	inlines = [
		ProductSpecificationsInline,
	]


class ProductImageInline(admin.TabularInline):
	model = ProductImage


class ProductSpecificationValueInline(admin.TabularInline):
	model = ProductSpecificationValue

@admin.register(Product)
class ProductTypeAdmin(admin.ModelAdmin):
	inlines = [
		ProductSpecificationValueInline,
		ProductImageInline,
	]
