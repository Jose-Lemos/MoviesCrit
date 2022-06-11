"""integrador2022 URL Configuration

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

from django.urls import path
from administracion.views import ActoresDetailView, PeliculasListView, ActoresListView, DirectoresListView, PeliculasDetailView, DirectoresDetailView

urlpatterns = [
    path('', PeliculasListView.as_view(), name="peliculas"),
    path('actores/', ActoresListView.as_view(), name="actores"),
    path('directores/', DirectoresListView.as_view(), name="directores"),
    path('pelicula/<pk>/', PeliculasDetailView.as_view(), name="detalles-pelicula"),
    path('actores/<pk>/', ActoresDetailView.as_view(), name="detalles-actor"),
    path('directores/<pk>/', DirectoresDetailView.as_view(), name="detalles-director"),
]
