from django.conf import settings
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), # ADD NEW PATTERN!
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^engaged/$', views.engaged, name='engaged'),
    url(r'^engaged2/$', views.engaged2, name='engaged2'),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^favorite/', views.favorite, name='favorite'),
    url(r'^posted/', views.posted, name='posted'),
	url(r'^(?P<event_id>[0-9]+)/showcsv/$', views.showcsv, name='showcsv'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^user_profile/$', views.user_profile, name='user_profile'),
    url(r'^chapass/$', views.chapass, name='chapass'),
    # user_id has to be identical to the db 
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^user_profile/$', views.user_profile, name='user_profile'),
    url(r'^map/$', views.map, name='map'),
    url(r'^dmap/$', views.dmap, name='dmap'),
    url(r'^homepage/$', views.homepage, name='homepage'),
	url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root':settings.STATIC_ROOT }),
    ]
