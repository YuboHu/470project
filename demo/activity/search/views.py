from django.shortcuts import render, render_to_response,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.utils import timezone
from events.models import Events, EventsCreater 
import datetime

def search(request):
	context= RequestContext(request)
	events_list = set()
	#eventspub_list= EventsPubdate.objects.select_related('events')
	#for e in EventsPubdate.objects.order_by('pubdate').select_related('events'):
	#	events_list.add(e.events)
	#print(events_list)
	#time=0
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
		events_list_wc= Events.objects.filter(starttime__lt=start).filter(starttime__gt=now).filter(title__contains=title).filter(location__contains=location).order_by('-pubdate')
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
						events_list.add(e)
			if enabledsports:
				for e in events_list_wc:
					if e.sports==True:
						events_list.add(e)
			if enabledfood:
				for e in events_list_wc:
					if e.food==True:
						events_list.add(e)
			if enabledparties:
				for e in events_list_wc:
					if e.party==True:
						events_list.add(e)
			if enabledarts:
				for e in events_list_wc:
					if e.arts==True:
						events_list.add(e)
			if enabledbus:
				for e in events_list_wc:
					if e.business==True:
						events_list.add(e)
		else:
			events_list=events_list_wc

		search = True

	return render_to_response(
            'search/search.html',
            {'events_list': events_list, 'search':search}, context)
