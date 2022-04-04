from app1.views import *
"""instagram_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xyz/', xyz),
    path('login/', login),
    path('signup/', signup),
    path('signup_page/', signup_page),
    path('login_page/', login_page),
    path('otp_verify/', otp_verify),
    path('profile/', profile),
    path('getupdatevalue/', getupdatevalue),
    path('updateprofile/',updateprofile),

]
