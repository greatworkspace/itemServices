from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'
		# fields = ["item_name", "item_barcode", "description",
		#  "frac", "purchasing_price", "purchasing_unit", "sales_price", "sales_unit"]