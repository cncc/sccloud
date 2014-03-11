from django.conf.urls import patterns, url

from slsync import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
    url(r'^200\/$', views.detail, name='detail')
)

