"""webproject URL Configuration

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
from django.urls import path
from webproject.views import webproject
from webproject.views import index, contacto, descargas, donaciones, legales, quienes_somos, tutoriales, tutoriales_especiales, header, footer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', webproject),
    path('index.html', index),
    path('contacto.html', contacto),
    path('descargas.html', descargas),
    path('donaciones.html', donaciones),
    path('legales.html', legales),
    path('quienes_somos.html', quienes_somos),
    path('tutoriales.html', tutoriales),
    path('tutoriales_especiales.html', tutoriales_especiales),
    path('header.html', header),
    path('footer.html', footer),
]
