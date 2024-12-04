"""
URL configuration for sports_club project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
from django.contrib.auth import views as auth_views
from members import views as member_views
from events import views as event_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', event_views.home, name='home'),  # Make sure you have a 'home' view in events/views.py
    path('register/', member_views.register, name='register'),
    path('login/', member_views.user_login, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('events/', include('events.urls')),
    path('facilities/', include('facilities.urls')),
    path('logout/', member_views.user_logout, name='logout')
]
