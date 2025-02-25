"""
URL configuration for profileapp project.

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
from operator import index
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from grav import settings
from . import views
from profileapp.views import login_view, logout_view, register_view
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_view, name='index'),
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/',views.edit_profile_view, name='edit_profile'),
    path('register/',views.register_view, name='register'),
    path('login/',views.login_view, name='login'),
    path('home/',views.home_view, name='home'),
    path('logout/', logout_view, name='logout'),
     path('login/', auth_views.LoginView.as_view(), name='login'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

