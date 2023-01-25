from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Products

# Create your views here.

@csrf_exempt
def productApi(request):
	#get all data from the database and return 200 Ok
	if request.method == 'GET':
		products = Products.objects.all()
		product_serializer = ProductSerializer(products, many = True )
		return JsonResponse(product_serializer.data, safe = False)
	#post request to the database and save, return 200k
	elif request.methos == 'POST':
		product_data= JSONParser().parse(request)
		product_serializer = ProductSerializer(data=product_data)
		if product_serializer.is_valid():
			product_serializer.save()
			return JsonResponse("Successfully Added", safe = False)
		return JsonResponse("Failed to Add", safe = False)
	#adjust data through put request in the database 
	elif request.method == 'PUT':
		product_data = JsonParse().parse(request)
		product=Products.objects.get(ProductId = product_data['ProductId'])
		products_serializer = ProductSerializer(product, data=product_data)
		if products_serializer.is_valid():
			products_serializer.save()
			return JsonResponse("Update Successfully", safe = false)
		return JsonResponse("Failed to Update")


# Using class based views

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



