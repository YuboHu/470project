from django.conf.urls import include, url	
from . import views

urlpatterns=[
	url(r'^aboutus/$', views.aboutus, name='aboutus'),

]