from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), # ADD NEW PATTERN!
    url(r'^regist/$', views.regist, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^some_view/', views.some_view, name='some_view'),
    url(r'^engaged/$', views.engaged, name='engaged'),
    url(r'^favorite/', views.favorite, name='favorite'),
    url(r'^posted/', views.posted, name='posted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^user_profile/$', views.user_profile, name='user_profile'),
	url(r'^chapass/$', views.chapass, name='chapass'),
	# user_id has to be identical to the db 
	url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<user_id>[0-9]+)/user_profile/$', views.user_profile, name='user_profile'),
	url(r'^map/$', views.map, name='map'),
	url(r'^dmap/$', views.dmap, name='dmap'),

    ]
