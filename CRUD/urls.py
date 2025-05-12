"""
URL configuration for CRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import re_path,path
from CRUDapp.views import *
urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r'^$',display),
    re_path(r'^insert/',insert),
    re_path(r'^delete/(?P<id>\d+)',delete),
    re_path(r'update/(?P<id>\d+)',update),
    #API endpoints
    path('api/students/', StudentList.as_view(), name='student-list'),
    path('api/students/<int:id>/', StudentDetail.as_view(), name='student-detail')
]
