from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ["category", "group", "sub_group", "brand_name", "item"]