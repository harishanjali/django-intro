from django.urls import path
from . import views

urlpatterns = [
    path('',views.calculate),
    path('mtable/',views.mtable)
]