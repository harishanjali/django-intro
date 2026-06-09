from django.urls import path
from . import views


urlpatterns = [
    path('add/',views.Calculator.as_view()),
    path('insert/',views.InsertView.as_view()),
    path('update/<int:pk>',views.ModifyView.as_view()),
    path('view/',views.SeeListView.as_view(),name='products-list'),
    path('delete/<int:pk>',views.MyDeleteView.as_view(),name='delete-product')
]