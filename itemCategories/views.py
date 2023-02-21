from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Product


# Create your views here.

# @api_view(['GET', 'POST', 'PUT'])
@csrf_exempt
def productApi(request, id=0):
	#get all data from the database and return 200 Ok
	if request.method == 'GET':
		products = Product.objects.all()
		product_serializer = ProductSerializer(products, many = True )
		return JsonResponse(product_serializer.data, safe = False)
	#post request to the database and save, return 200k
	elif request.method == 'POST':
		product_data = JSONParser().parse(request)
		product_serializer = ProductSerializer(data= product_data)
		if product_serializer.is_valid():
			product_serializer.save()
			# return JsonResponse(product_serializer.data, status = status.HTTP_201_CREATED)
			return JsonResponse("Added Successfully", safe = False)
		return JsonResponse("Item not saved, failed to Add", safe = False)
	#adjust data through put request in the database 
	elif request.method == 'PUT':
	 	product_data = JSONParser().parse(request)
	 	product=Product.objects.get(id = product_data['id'])
	 	products_serializer = ProductSerializer(product, data=product_data)
	 	if products_serializer.is_valid():
			 products_serializer.save()
			 return JsonResponse("Update Successfully", safe = False)
	 	return JsonResponse("Failed to Update")
	#the delete method
	elif request.method == 'DELETE':		
		product_data=JSONParser().parse(request)
		product = Product.objects.get(id = product_data['id'])
	 	
		product.delete()
		return JsonResponse("Deleted Successfully", safe = False)


# Using class based views
#product=Product.objects.get(id=product_data['id'])# product = Product.objects.get(id = id)
# product = Product.objects.get(id = id)
# class ProductListApiView(APIView):
# 	def post(self, request, *args, **kwargs):

# 	#Create an item with the list and their categories
	
# 		data = {
# 			'item': request.data.get('item'),
# 			'brand_name': request.data.get('brand_name'),
# 			'sub_group': request.data.get('sub_group'),
# 			'group': request.data.get('group'),
# 			'category': request.data.get('category')
# 		}
# 		serializer = ProductSerializer(data = data)

# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_created)

# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



