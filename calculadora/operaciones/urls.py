from django.urls import path

from . import views

app_name = "operaciones"
urlpatterns = [
    path('', views.math_operation, name='math_operation'),
]
