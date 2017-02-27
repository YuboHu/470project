from django.shortcuts import render, render_to_response,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.utils import timezone
from events.models import Events, EventsCreater 
from users.models import UserProfile
import datetime


def search(request):
	context= RequestContext(request)
	user=request.user
	
	events_list = list()
	today=datetime.date.today()
	#eventspub_list= EventsPubdate.objects.select_related('events')
	#for e in EventsPubdate.objects.order_by('pubdate').select_related('events'):
	#	events_list.append(e.events)
	#print(events_list)
	#time=0
	if user.is_active:
		userprofile=UserProfile.objects.get(user=user)
		age=today.year-userprofile.birthday.year
		m=today.month-userprofile.birthday.month
		if today.day-userprofile.birthday.day<0:
			m-=1
		if m<0:
			age-=1
	else:
		age=16
    	search = False

    # If it's a HTTP POST, we're interested in processing form data.
    	if request.method == 'POST':
		
        	title=request.POST['Title']
		location=request.POST['Location']
		time=request.POST['Time']
		if time == '0':
			time = 365
		now=timezone.now()
		start=timezone.now() + datetime.timedelta(days=int(time))
		events_list_wc= Events.objects.filter(starttime__lt=start).filter(starttime__gt=now).filter(title__contains=title).filter(location__contains=location).filter(age_limit__lte=age).order_by('-pubdate')#.order_by('engaged_people')
		#events_list=set()
		enabledmusic = bool(request.POST.get('isMusic'))
              	enabledsports = bool(request.POST.get('isSports'))
               	enabledfood = bool(request.POST.get('isFooddrink'))
               	enabledparties = bool(request.POST.get('isParties'))
               	enabledarts = bool(request.POST.get('isArts'))
                enabledbus = bool(request.POST.get('isBusniess'))
		if enabledmusic or enabledsports or enabledfood or enabledparties or enabledarts or enabledbus:
			#events_list=events_list_wc
			if enabledmusic:
				for e in events_list_wc:
					if e.music==True:
						events_list.append(e)
			if enabledsports:
				for e in events_list_wc:
					if e.sports==True:
						events_list.append(e)
			if enabledfood:
				for e in events_list_wc:
					if e.food==True:
						events_list.append(e)
			if enabledparties:
				for e in events_list_wc:
					if e.party==True:
						events_list.append(e)
			if enabledarts:
				for e in events_list_wc:
					if e.arts==True:
						events_list.append(e)
			if enabledbus:
				for e in events_list_wc:
					if e.business==True:
						events_list.append(e)
		else:
			events_list=events_list_wc

		search = True

	return render_to_response(
            'search/search.html',
            {'events_list': events_list, 'search':search}, context)

def topsearch(request):
	context= RequestContext(request)
	user=request.user
	
	now=timezone.now()
	today=datetime.date.today()
	if user.is_active:
		userprofile=UserProfile.objects.get(user=user)
		age=today.year-userprofile.birthday.year
		m=today.month-userprofile.birthday.month
		if today.day-userprofile.birthday.day<0:
			m-=1
		if m<0:
			age-=1
	else:
		age=16
	events_list_wc= Events.objects.filter(starttime__gt=now).filter(age_limit__lte=age).order_by('-starttime')
	
	events_list=events_list_wc

	search = True

	return render_to_response(
            'search/search.html',
            {'events_list': events_list, 'search':search}, context)


def partysearch(request):
	context= RequestContext(request)
	user=request.user
	today=datetime.date.today()
	
	if user.is_active:
		userprofile=UserProfile.objects.get(user=user)
		age=today.year-userprofile.birthday.year
		m=today.month-userprofile.birthday.month
		if today.day-userprofile.birthday.day<0:
			m-=1
		if m<0:
			age-=1
	else:
		age=16
	now=timezone.now()

	events_list_wc= Events.objects.filter(starttime__gt=now).filter(age_limit__lte=age).filter(party=True).order_by('-starttime')
	
	events_list=events_list_wc

	search = True

	return render_to_response(
            'search/search.html',
            {'events_list': events_list, 'search':search}, context)


def musicsearch(request):
	context= RequestContext(request)
	user=request.user
	today=datetime.date.today()
	
	if user.is_active:
		userprofile=UserProfile.objects.get(user=user)
		age=today.year-userprofile.birthday.year
		m=today.month-userprofile.birthday.month
		if today.day-userprofile.birthday.day<0:
			m-=1
		if m<0:
			age-=1
	else:
		age=16
	now=timezone.now()

	events_list_wc= Events.objects.filter(starttime__gt=now).filter(age_limit__lte=age).filter(music=True).order_by('-starttime')
	
	events_list=events_list_wc

	search = True

	return render_to_response(
            'search/search.html',
            {'events_list': events_list, 'search':search}, context)


def sportsearch(request):
	context= RequestContext(request)
	user=request.user
	today=datetime.date.today()
	
	if user.is_active:
		userprofile=UserProfile.objects.get(user=user)
		age=today.year-userprofile.birthday.year
		m=today.month-userprofile.birthday.month
		if today.day-userprofile.birthday.day<0:
			m-=1
		if m<0:
			age-=1
	else:
		age=16
	now=timezone.now()

	events_list_wc= Events.objects.filter(starttime__gt=now).filter(age_limit__lte=age).filter(sports=True).order_by('-starttime')
	
	events_list=events_list_wc

	search = True

	return render_to_response(
            'search/search.html',
            {'events_list': events_list, 'search':search}, context)


def food_drinksearch(request):
	context= RequestContext(request)
	user=request.user
	today=datetime.date.today()
	
	if user.is_active:
		userprofile=UserProfile.objects.get(user=user)
		age=today.year-userprofile.birthday.year
		m=today.month-userprofile.birthday.month
		if today.day-userprofile.birthday.day<0:
			m-=1
		if m<0:
			age-=1
	else:
		age=16
	now=timezone.now()

	events_list_wc= Events.objects.filter(starttime__gt=now).filter(age_limit__lt=age).filter(food=True).order_by('-starttime')
	
	events_list=events_list_wc

	search = True

	return render_to_response(
            'search/search.html',
            {'events_list': events_list, 'search':search}, context)


def artsearch(request):
	context= RequestContext(request)
	user=request.user
	today=datetime.date.today()
	
	if user.is_active:
		userprofile=UserProfile.objects.get(user=user)
		age=today.year-userprofile.birthday.year
		m=today.month-userprofile.birthday.month
		if today.day-userprofile.birthday.day<0:
			m-=1
		if m<0:
			age-=1
	else:
		age=16
	now=timezone.now()

	events_list_wc= Events.objects.filter(starttime__gt=now).filter(age_limit__lte=age).filter(arts=True).order_by('-starttime')
	
	events_list=events_list_wc

	search = True

	return render_to_response(
            'search/search.html',
            {'events_list': events_list, 'search':search}, context)


def bus_search(request):
	context= RequestContext(request)
	user=request.user
	today=datetime.date.today()
	
	if user.is_active:
		userprofile=UserProfile.objects.get(user=user)
		age=today.year-userprofile.birthday.year
		m=today.month-userprofile.birthday.month
		if today.day-userprofile.birthday.day<0:
			m-=1
		if m<0:
			age-=1
	else:
		age=16
	now=timezone.now()

	events_list_wc= Events.objects.filter(starttime__gt=now).filter(age_limit__lte=age).filter(business=True).order_by('-starttime')
	
	events_list=events_list_wc

	search = True

	return render_to_response(
            'search/search.html',
            {'events_list': events_list, 'search':search}, context)
