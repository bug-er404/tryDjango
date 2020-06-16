from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import(
    EmployeeActions,
    EmployeeListCreate,
)

urlpatterns = {

    path('',EmployeeListCreate.as_view()),
    path('<int:pk>/', EmployeeActions.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)