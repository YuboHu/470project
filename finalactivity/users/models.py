from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.
class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	#birthdate = models.DateField(blank=True,null=True)
	# The additional attributes we wish to include.
	#your_password = models.CharField(max_length=20, blank=True, null=True)
	#birthday = models.DateField(blank=True, default = datetime.datetime.now().date)
	#birthday = models.DateField(blank=False)

	birthday = models.DateField(blank=False)
	
	make_public_your_user_name = models.BooleanField(default=True)
	#picture = models.ImageField(upload_to='profile_images', blank=True)
	
	street_number = models.CharField(max_length=20, null=True, blank=True)

	street_name = models.CharField(max_length=20, null=True, blank=True)

	city_name = models.CharField(max_length=20, null=True, blank=True)

	province_name = models.CharField(max_length=20, null=True, blank=True)

	postal_code = models.CharField(max_length=20, null=True, blank=True)

	country_name = models.CharField(max_length=20, null=True, blank=True)
	
	latitude = models.CharField(max_length=20, null=True, blank=True)
	
	longitude = models.CharField(max_length=20, null=True, blank=True)

	#the following is preference--------
	isMusic = models.BooleanField(default=False)

	isSports = models.BooleanField(default=False)

	isFood_Drink = models.BooleanField(default=False)

	isParties = models.BooleanField(default=False)

	isArts = models.BooleanField(default=False)

	isBusiness = models.BooleanField(default=False)

	# the phone number field
	phonenumber = models.CharField(max_length=20, null=True, blank=True)

	# the gender field
	isMale = models.BooleanField(default=True)

	isFemale = models.BooleanField(default=False)


	def __unicode__(self):
		return self.user.username
