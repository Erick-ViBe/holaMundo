from django.urls import path
from .views import home_view, sum_view, create_task

urlpatterns = [
    path('', home_view, name='home'),
    path('suma/<int:num1>/<int:num2>/', sum_view, name='sum'),
    path('create_task/<str:description>/', create_task, name='create-task'),
]