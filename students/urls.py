from django.urls import path
from . import views


urlpatterns = [
    path('',views.students_app),
    path('about/',views.students_about)
]