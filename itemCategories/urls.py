#from django.conf.urls import url
from django.urls import path, include
from .views import (ProductListApiView,)

urlpatterns = [
	path('api', ProductListApiView.as_view()),
]