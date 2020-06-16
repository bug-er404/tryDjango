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
from .views import *
app_name = "main_contact"

urlpatterns = [
    path('', contact_list_function_view, name='contact_list'),
    path('create/', contact_create_function_view, name='contact_create'),
    path('<str:my_title>/',contact_detail_function_view, name='contact_detail'),
    path('<str:my_title>/delete/',contact_delete_function_view, name='contact_delete'),
]
