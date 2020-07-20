from django.urls import path,include
from .views import (
	index,

	)

app_name='product'

urlpatterns = [
	path('', index, name='index'),
]
