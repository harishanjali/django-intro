from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('productset',views.ProductsViewSet,basename='product')

urlpatterns = [
    path('products/',views.ProductApi.as_view()),
    path('products/<int:pk>/',views.UpdateProductApi.as_view()),
    path('customproduct/',views.CustomProductApi.as_view()),
    path('customproduct/<int:pk>/',views.ModifyCustomProductApi.as_view())
]

urlpatterns = urlpatterns + router.urls