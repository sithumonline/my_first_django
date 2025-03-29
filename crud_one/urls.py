from django.urls import path
from .views import index, create, pre_update, update, delete

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('pre_update/<int:id>/', pre_update, name='pre_update'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
]
