from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
	name = models.CharField(
		verbose_name='Название категории',
		help_text='Обязательное поле',
		max_length=255,
		unique=True,
	)
	slug = models.SlugField(max_length=255, unique=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	is_active = models.BooleanField(default=True)
	is_boop = models.BooleanField(default=False)
	
	class MPTTMeta:
		order_insertion_by = ['name']
	
	class Meta:
		verbose_name = ('Категория')
		verbose_name_plural = ('Категории')
	
	# def get_absolute_url(self):
	# 	return reverse('products:category_list', args=[self.slug])
	
	def __str__(self):
		return self.name


class ProductType(models.Model):
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	
	def __str__(self):
		return self.name


class ProductSpecification(models.Model):
	product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
	name = models.CharField(max_length=255)
	
	def __str__(self):
		return self.name


class Product(models.Model):
	product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
	category = models.ForeignKey(Category, on_delete=models.RESTRICT)
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	slug = models.SlugField(max_length=255)
	regular_price = models.DecimalField(max_digits=6, decimal_places=2)
	discount_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, )
	
	class Meta:
		ordering = ['-created_at']
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
	
	# def get_absolute_url(self):
	# 	return reverse('products:product_detail', args=[self.slug])
	
	def __str__(self):
		return self.title


class ProductSpecificationValue(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	specification = models.ForeignKey(ProductSpecification, on_delete=models.RESTRICT)
	value = models.CharField(max_length=255)
	
	def __str__(self):
		return self.value


class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
	image = models.ImageField(upload_to='images/', default='images/placeholder.png')
	alt_text = models.CharField(max_length=255, null=True, blank=True)
	is_feature = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, )
