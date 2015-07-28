from django.conf.urls import include, url	
from . import views

urlpatterns=[
	url(r'^post/$', views.post, name='post'),
	url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<event_id>[0-9]+)/engage/$', views.engage, name='engage'),
	url(r'^(?P<event_id>[0-9]+)/dis_engage/$', views.dis_engage, name='dis_engage'),
	url(r'^(?P<event_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
	url(r'^(?P<event_id>[0-9]+)/dis_favorite/$', views.dis_favorite, name='dis_favorite'),
	#url(r'^map/$', views.map, name='map'),
	url(r'^cmap/$', views.cmap, name='cmap'),
]
