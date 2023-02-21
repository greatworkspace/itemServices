from django.conf.urls import url
#from django.urls import path, include
#from .views import (ProductListApiView,)
from itemCategories import views


urlpatterns = [
	url(r'^api$', views.productApi),
	url(r'^api/([0-9]+)$', views.productApi)
]