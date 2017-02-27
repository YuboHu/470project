from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Events(models.Model):
	
	
	title = models.CharField(max_length=300)
	#location = models.CharField(max_length=300)
	#endtime=models.DateTimeField('End time')
	#location= models.CharField(max_length=300)
	brief_intro= models.TextField('Brief Introduction')
	poster=models.ImageField(upload_to='poster_images', blank=True)
	organizer= models.CharField(max_length=200)
	contact_email= models.EmailField(max_length=254)
	contact_phonenumber= models.CharField(max_length=20)
	capacity= models.IntegerField('Maximum number of people')
	engaged_people=models.IntegerField('Engaged people',default=0)
	age_limit= models.IntegerField('Age minimum limit')
	ticket=models.URLField()
	description=models.TextField()
	
	#EventsTime
	starttime= models.DateTimeField('Start time')
	endtime=models.DateTimeField('End time')

	#EventsCategory
	
	music=models.BooleanField(default=False)
	sports=models.BooleanField(default=False)
	food=models.BooleanField(default=False)
	party=models.BooleanField(default=False)
	arts=models.BooleanField(default=False)
	business=models.BooleanField(default=False)

	#EventsLocation
	location= models.CharField(max_length=300)
	street_number = models.CharField(max_length=20, null=True, blank=True)
	street_name = models.CharField(max_length=20, null=True, blank=True)
	city_name = models.CharField(max_length=20, null=True, blank=True)
	province_name = models.CharField(max_length=20, null=True, blank=True)
	postal_code = models.CharField(max_length=20, null=True, blank=True)
	country_name = models.CharField(max_length=20, null=True, blank=True)
	latitude = models.CharField(max_length=20, null=True, blank=True)
	longitude = models.CharField(max_length=20, null=True, blank=True)
	#EventsPubdate
	pubdate= models.DateTimeField('Date published',null=True)
	updatedate= models.DateTimeField('Date updated',null=True)
	def __unicode__(self):
		return self.title

class EventsCreater(models.Model):
	events= models.OneToOneField(Events)
	creater=models.ForeignKey(User)
	createdate= models.DateTimeField('Date published',null=True)

class Engagement(models.Model):
	user = models.ForeignKey(User)
	event = models.ForeignKey(Events)
	engage_time = models.DateTimeField()
	is_engage = models.BooleanField(default = True)
	def __unicode__(self):
		return self.user_id

class Bookmark(models.Model):
	user = models.ForeignKey(User)
	event = models.ForeignKey(Events)
	is_favorite = models.BooleanField(default = True)
	def __unicode__(self):
		return self.event_id

class Comments(models.Model):
	user = models.ForeignKey(User)
	event = models.ForeignKey(Events)
	comments = models.TextField()
	comments_time = models.DateTimeField()
	name_public = models.BooleanField(default=True);
	like_num = models.IntegerField(default=0)
	dislike_num = models.IntegerField(default=0)
	def __unicode__(self):
		return self.event_id
