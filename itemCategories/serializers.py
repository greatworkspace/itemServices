from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Products
		fields = ["category", "group", "sub_group", "brand_name", "item"]