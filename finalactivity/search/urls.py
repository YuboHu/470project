from django.conf.urls import include, url	
from . import views

urlpatterns=[
	url(r'^search/$', views.search, name='search'),
	url(r'^topsearch/$', views.topsearch, name='topsearch'),
	url(r'^partysearch/$', views.partysearch, name='partysearch'),
	url(r'^musicsearch/$', views.musicsearch, name='musicsearch'),
	url(r'^sportsearch/$', views.sportsearch, name='sportsearch'),
	url(r'^food_drinksearch/$', views.food_drinksearch, name='food_drinksearch'),
	url(r'^artsearch/$', views.artsearch, name='artsearch'),
	url(r'^bus_search/$', views.bus_search, name='bus_search'),



]
