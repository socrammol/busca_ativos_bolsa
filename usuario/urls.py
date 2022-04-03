from django.urls import path
from .views import *




urlpatterns = [
    path('', list_usuario, name='list_usuario'),
    path('new', create_usuario, name='create_usuario'),
    path('update/<int:id>/', update_usuario, name='update_usuario'),
    path('delete/<int:id>/', delete_usuario, name='delete_usuario'),
]
