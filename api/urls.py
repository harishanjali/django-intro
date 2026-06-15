from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.ProductApi.as_view()),
    path('products/<int:pk>/',views.UpdateProductApi.as_view()),
    path('customproduct/',views.CustomProductApi.as_view()),
    path('customproduct/<int:pk>/',views.ModifyCustomProductApi.as_view())
]
