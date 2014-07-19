from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.static import serve
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^f/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
)
