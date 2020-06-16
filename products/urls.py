"""demoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from products.views import (simple_function_view_response, simple_function_view_render_default, contact_function_view, product_detail_function_view,product_create_function_view,
                            product_list_function_view, product_delete_function_view)

app_name = "main_product"

urlpatterns = [
    path('', product_list_function_view, name = 'product_list'),
    path('create/', product_create_function_view, name='product_create'),
    path('<str:my_title>/',product_detail_function_view, name ='product_detail'),
    path('<str:my_title>/delete/',product_delete_function_view, name='product_delete'),

    # path('/api', product_apiview_1),
    # path('api/createapi', product_apiview_2),
    # path('/api/<str:my_slug>/', product_apiview_3),
    # path('/api/<str:my_slug>/delete/', product_apiview_4),
]
