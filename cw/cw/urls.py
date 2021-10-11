"""cw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from codingwars import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('hello/', views.main_page, name="main_page"),
    path('time/', views.watch_now, name="time"),
    path('subject_names/', views.subject_names, name="subject_names"),
    path('create_subject/', views.create_subject, name="create_subject"),
    path('uroki/<int:subject_id>/', views.uroki, name="uroki"),
    path('create_urok/<int:subject_id>/', views.create_urok, name="create_urok"),
    path('delete_subject/<int:subject_id>/', views.delete_subject, name="delete-subject"),
    path('delete_urok/<int:urok_id>/', views.delete_urok, name="delete-urok"),
]