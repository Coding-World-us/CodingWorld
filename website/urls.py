"""website URL Configuration

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
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.Home),
    path('contact' , views.Contact),
    path('about' , views.About),
    path('playlists' , views.Playlists),
    path('python-tutorial-0' , views.Python_Video_0),
    path('file-0' , views.video_0),
    path('python-tutorial-1' , views.Python_Video_1),
    path('file-1' , views.video_1),
    path('python-tutorial-2' , views.Python_Video_2),
    path('file-2' , views.video_2),
] + static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
