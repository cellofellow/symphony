from django.conf.urls import url, include
from django.contrib import admin

from library.views import (SearchView, PieceDetail, LocationView,
                           PerformanceList)

urlpatterns = [
    url(r'^$', SearchView.as_view()),
    url(r'^performances/$', PerformanceList.as_view(), name='performance_list'),
    url(r'^(?P<pk>[0-9]+)/$', PieceDetail.as_view(), name='piece_detail'),
    url(r'^location/(?P<pk>[0-9]+)/$', LocationView.as_view(), name='location_detail'),
    url(r'^admin/', admin.site.urls),
]
