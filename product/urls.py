from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create,name='create'),
    path('view/',views.view,name='view'),
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:pk>/',views.delete,name='delete')
]