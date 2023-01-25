#from django.conf.urls import url
from django.urls import path, include
#from .views import (ProductListApiView,)
from itemCategories import views


urlpatterns = [
	path('api', views.productApi),
]