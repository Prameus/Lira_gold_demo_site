"""lira_gold_site2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from products.views import *
from authentication_management.views import *
from pages.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set_password/',
         auth_views.PasswordChangeView.as_view(template_name='set_password.html')),
    path('set_password_success/', set_password_success,
         name='set_password_success'),

    path('',home),
    path('cart/',cart),
    path('profile/',profile),


    path('register/', register_user),
    path('login/', login_user),
    path('member/', include('django.contrib.auth.urls')),

    path('search_page/', search_page, name='search-page'),
    path('update_item/', update_item)
] + static(settings.MEDIA_URL, document_root=settings.IMAGE_ROOT)
