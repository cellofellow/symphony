"""symphony URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from library.views import SearchView, PieceDetail, LocationView

urlpatterns = [
    url(r'^$', SearchView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', PieceDetail.as_view(), name='piece_detail'),
    url(r'^location/(?P<pk>[0-9]+)/$', LocationView.as_view(), name='location_detail'),
    url(r'^admin/', admin.site.urls),
]
