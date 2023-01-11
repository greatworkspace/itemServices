#from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Product
from rest_framework.views import APIView

# Create your views here.
# Using class based views

class ProductListApiView(APIView):
	def post(self, request, *args, **kwargs):

	#Create an item with the list and their categories
	
		data = {
			'item': request.data.get('item'),
			'brand_name': request.data.get('brand_name'),
			'sub_group': request.data.get('sub_group'),
			'group': request.data.get('group'),
			'category': request.data.get('category')
		}
		serializer = ProductSerializer(data = data)

		if serializer.is_valid():
			serializer.save()
			return Reponse(serializer.data, status=status.HTTP_201_created)

		return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



