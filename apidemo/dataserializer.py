from django import forms
from .models import Employees
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"
