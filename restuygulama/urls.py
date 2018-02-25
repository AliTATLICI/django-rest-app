"""restuygulama URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from django.contrib import admin
from pbs import views
from rest_framework.authtoken import views as vw


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('pbs/', include('pbs.urls')),
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('pbs/', views.Index.as_view()),
    path('v1/transaksi/', views.Transaksi.as_view()),
    path('v1/transaksi/<int:transaksi_id>', views.TransaksiModifikasi.as_view()),
    path('register/', views.Register.as_view()),
    path('change_password/', views.ChangePassword.as_view()),
    path('login/', vw.obtain_auth_token)
]

