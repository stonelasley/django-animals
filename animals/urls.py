from django.conf.urls import patterns, url

from animals import views

urlpatterns = patterns('',
                       url(r'^$',
                           views.Index.as_view(),
                           name='index'),
                       url(r'^(?P<pk>\d+)/$',
                           views.AnimalDetail.as_view(),
                           name='detail'),
                       url(r'^(?P<pk>\d+)/update/$',
                           views.AnimalUpdate.as_view(),
                           name='update'),
                       url(r'^create/$',
                           views.AnimalCreate.as_view(),
                           name='create'),
                       url(r'^(?P<pk>\d+)/delete/$',
                           views.AnimalUpdate.as_view(),
                           name='delete'),
                       )
