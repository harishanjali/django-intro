"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from intro.views import SignupView

urlpatterns = [
    #debug tool bar always first
    path('__debug__/',include("debug_toolbar.urls")),
    #admin url
    path('admin/', admin.site.urls),

    # 1. Standard Login and Logout routes
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #for signup
    path('signup/',SignupView.as_view(template_name='registration/signup.html'),name='signup'),

    #app urls
    path('',include('intro.urls')),
    path('hari/',include('firstApp.urls')),
    path('calculator/',include('calculator.urls')),
    path('student/',include('student.urls')),
    path('students/',include('students.urls')),
    path('product/',include('product.urls')),
    path('addition/',include('addition.urls')),
    path('class/',include('classApp.urls')),
    path('api/',include('api.urls')),
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)