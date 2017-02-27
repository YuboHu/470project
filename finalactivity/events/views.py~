from django.shortcuts import render, render_to_response,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from events.models import Events, EventsCreater,Engagement, Bookmark
from events.forms import EventsForm
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import UserProfile
from events.models import Comments
from django.core.mail import send_mail, BadHeaderError
from dateutil import tz
from django.contrib import messages

from reportlab.pdfgen import canvas
from io import BytesIO
from django.utils import timezone
import datetime
import os
from django.conf import settings

from django.contrib.auth.decorators import login_required

import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def post(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    user=request.user
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    posted = False

    if request.method == 'POST':
	event = Events()
	event.title = request.POST['title']
	event.brief_intro = request.POST['brief_intro']
	event.organizer = request.POST['organizer']
	event.contact_email = request.POST['contact_email']
	event.contact_phonenumber = request.POST['contact_phonenumber']
	event.capacity = request.POST['capacity']
	event.age_limit = request.POST['age_limit']
	event.ticket = request.POST['ticket']
	event.description = request.POST['description']
	event.starttime = request.POST['starttime']
	event.endtime = request.POST['endtime']

        event.music = bool(request.POST.get('isMusic'))
        event.sports = bool(request.POST.get('isSport'))
        event.food = bool(request.POST.get('isFood'))
        event.party = bool(request.POST.get('isParty'))
        event.arts = bool(request.POST.get('isArts'))
        event.busniess = bool(request.POST.get('isBusniess'))

	if 'poster' in request.FILES:
		event.poster = request.FILES['poster']
	event.pubdate= timezone.now()
	event.updatedate= timezone.now()
	event.street_number = request.POST['street_number_']
	event.street_name = request.POST['street_name_']
	event.city_name = request.POST['city_name_']
	event.province_name = request.POST['province_name_']
	event.postal_code = request.POST['postal_code_']
	event.country_name = request.POST['country_name_']
	event.latitude = request.POST['latitude_']
	event.longitude = request.POST['longitude_']
	event.location = request.POST['location_']
	event.save()
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # Thi s delays saving the model until we're ready to avoid integrity problems.
            
	    #user = get_object_or_404(UserProfile, pk=user.user_id)
	EventsCreater.objects.create(events=event,creater=user, createdate=timezone.now())
            # Update our variable to tell the template registration was successful.
	posted = True
	from_zone = tz.gettz('UTC')
	to_zone = tz.gettz('America/Vancouver')
	_event = get_object_or_404(Events, pk=event.id)
    
	_starttime = _event.starttime
	#_starttime = datetime.datetime.strptime(_starttime, '%Y-%m-%dT%H:%M')
	#_starttime = _starttime.replace(tzinfo=from_zone)
	_localtime = _starttime.astimezone(to_zone)

	_endtime = _event.endtime
	#_endtime = datetime.datetime.strptime(_endtime, '%Y-%m-%dT%H:%M')
	_localtime2 = _endtime.astimezone(to_zone)
	subject = '[QuickActivity - Do Not Reply] You Have Posted an Activity!'
	message = 'Hi ' + user.username + ',\n\n' + 'You have successfully posted the activity ' + event.title +'. The starting time is ' + unicode(_localtime) + ', ending time is ' + unicode(_localtime2) + ', and the location is ' + event.location + '.\n\nYours,\nQuickActivity Team\n'
	try:
		send_mail(subject, message, 'cmpt470group6@gmail.com', [user.email], fail_silently=True)
	except BadHeaderError:
		return HttpResponse('Invalid header found.')
        # Invalid form or forms - mistakes or somethi ng else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        #else:
        #   print events_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.

    # Render the template depending on the context.
    return render_to_response(
            'events/post.html',
            {'posted': posted}, context)

@login_required
def edit(request,event_id):
    # Like before, get the request's context.
    context = RequestContext(request)
    user=request.user
    event = get_object_or_404(Events, pk=event_id)
    if EventsCreater.objects.filter(creater=user,events=event).count()==0 or event.starttime<timezone.now():
	permission= False
    else:
	permission= True    

    edited=False
 	
    if request.method == 'POST':
	event= get_object_or_404(Events, pk=event_id)
	event.title = request.POST['title']
	event.brief_intro = request.POST['brief_intro']
	event.organizer = request.POST['organizer']
	event.contact_email = request.POST['contact_email']
	event.contact_phonenumber = request.POST['contact_phonenumber']
	event.capacity = request.POST['capacity']
	event.age_limit = request.POST['age_limit']
	event.ticket = request.POST['ticket']
	event.description = request.POST['description']
	event.starttime = request.POST['starttime']
	event.endtime = request.POST['endtime']

        event.music = bool(request.POST.get('isMusic'))
        event.sports = bool(request.POST.get('isSport'))
        event.food = bool(request.POST.get('isFood'))
        event.party = bool(request.POST.get('isParty'))
        event.arts = bool(request.POST.get('isArts'))
        event.busniess = bool(request.POST.get('isBusniess'))

	if 'poster' in request.FILES:
		event.poster = request.FILES['poster']
	event.updatedate = timezone.now()
	event.street_number = request.POST['street_number_']
	event.street_name = request.POST['street_name_']
	event.city_name = request.POST['city_name_']
	event.province_name = request.POST['province_name_']
	event.postal_code = request.POST['postal_code_']
	event.country_name = request.POST['country_name_']
	event.latitude = request.POST['latitude_']
	event.longitude = request.POST['longitude_']
	event.location = request.POST['location_']
	event.save()

	from_zone = tz.gettz('UTC')
	to_zone = tz.gettz('America/Vancouver')
	_event = get_object_or_404(Events, pk=event_id)
	_starttime = _event.starttime
	#_starttime = _starttime.replace(tzinfo=from_zone)
	_localtime = _starttime.astimezone(to_zone)
	_endtime = _event.endtime
	_localtime2 = _endtime.astimezone(to_zone)
	subject = '[QuickActivity - Do Not Reply] You Have Updated an Activity!'
	message = 'Hi ' + user.username + ',\n\n' + 'You have successfully updated the activity ' + event.title +'. The starting time is ' + unicode(_localtime) + ', ending time is ' + unicode(_localtime2) + ', and the location is ' + event.location + '.\n\nYours,\nQuickActivity Team\n'
	try:
		send_mail(subject, message, 'cmpt470group6@gmail.com', [user.email], fail_silently=True)
	except BadHeaderError:
		return HttpResponse('Invalid header found.')
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # Thi s delays saving the model until we're ready to avoid integrity problems.
            
	    #user = get_object_or_404(UserProfile, pk=user.user_id)
        #$userprofile.gender = self.get_gender_display()
	edited = True
    

	
    return render_to_response('events/edit.html', {'permission': permission, 'event':event, 'edited': edited}, context)


def detail(request, event_id):
    if request.method == 'GET' and 'application/json' in request.META.get('HTTP_ACCEPT'):
        event_info = {}	
        _event = get_object_or_404(Events, pk=event_id)
        event_info["title"] = _event.title
        event_info["organizer"] = _event.organizer
        event_info["capacity"] = _event.capacity
        event_info["number of participants"] = _event.engaged_people
        event_info["start time in UTC"] = str(_event.starttime)
        event_info["end time in UTC"] = str(_event.endtime)
        event_info["location"] = _event.location
        event_info["ticket link"] = _event.ticket
        event_info["contact email"] = _event.contact_email
        event_info["contact phone"] = _event.contact_phonenumber
        event_info["category isMusic"] = _event.music
        event_info["category isSports"] = _event.sports
        event_info["category isFood"] = _event.food
        event_info["category isParty"] = _event.party
        event_info["category isArts"] = _event.arts
        event_info["category isBusiness"] = _event.business
        event_info["brief introduction"] = _event.brief_intro
        event_info["detailed description"] = _event.description
        event_info["update time in UTC"] = str(_event.updatedate)
        #info = HttpResponse()
        info = HttpResponse(content_type = "application/json")
        info['Content-Disposition'] = 'inline; filename="%s.json"'%(_event.title)
        #info.write(json.dumps(contact_info, sort_keys=True));
        info.write('{\n  "title": ' + json.dumps(event_info["title"]) + ', \n  "organizer": ' + json.dumps(event_info["organizer"]) + ', \n  "capacity": ' + json.dumps(event_info["capacity"]) + ', \n  "number of participants": ' + json.dumps(event_info["number of participants"]) + ', \n  "start time in UTC": ' + json.dumps(event_info["start time in UTC"]) + ', \n  "end time in UTC": ' + json.dumps(event_info["end time in UTC"]) + ', \n  "location": ' + json.dumps(event_info["location"]) + ', \n  "ticket link": ' + json.dumps(event_info["ticket link"]) + ', \n  "contact email": ' + json.dumps(event_info["contact email"]) + ', \n  "contact phone": ' + json.dumps(event_info["contact phone"]) + ', \n  "category isMusic": ' + json.dumps(event_info["category isMusic"]) + ', \n  "category isSports": ' + json.dumps(event_info["category isSports"]) + ', \n  "category isFood": ' + json.dumps(event_info["category isFood"]) + ', \n  "category isParty": ' + json.dumps(event_info["category isParty"]) + ', \n  "category isArts": ' + json.dumps(event_info["category isArts"]) + ', \n  "category isBusiness": ' + json.dumps(event_info["category isBusiness"]) + ', \n  "brief introduction": ' + json.dumps(event_info["brief introduction"]) + ', \n  "detailed description": ' + json.dumps(event_info["detailed description"]) + ', \n  "update time in UTC": ' + json.dumps(event_info["update time in UTC"]) + '\n}\n');
        return info;
    else:
        event1 = get_object_or_404(Events, pk=event_id)
        user=request.user
        #eventspub_list= EventsPubdate.objects.select_related('events')
        #for e in EventsPubdate.objects.order_by('pubdate').select_related('events'):
        #   events_list.append(e.events)
        #print(events_list)
        #time=0
        if user.is_active:
            userprofile=UserProfile.objects.get(user=user)
            today=datetime.date.today()
            age=today.year-userprofile.birthday.year
            m=today.month-userprofile.birthday.month
            if today.day-userprofile.birthday.day<0:
                m-=1
            if m<0:
                age-=1
        else:
            age=16
    
        if event1.age_limit>age:
            return render(request, 'users/noright.html')
        else:
            context = RequestContext(request)
        
            _event = get_object_or_404(Events, pk=event_id)
            if timezone.now() > _event.starttime:
                indate = False
            else:
                indate = True

            _user = request.user
            if _event.engaged_people == _event.capacity:
                _is_full = True
            else:
                _is_full = False

            _is_engage = True
            _is_favorite = True
    
            if _user.is_active:
                if Engagement.objects.filter(user=_user, event=_event).count() == 0:
                    _is_engage = False
                else:
                    _is_engage = True
            
                if Bookmark.objects.filter(user=_user, event=_event).count() == 0:
                    _is_favorite = False
                else:
                    _is_favorite = True
        
            _person_list = []
            _engage_list = Engagement.objects.filter(event=_event).order_by('-engage_time').select_related('user')[:20]
            for _engage in _engage_list:
                _infor = UserProfile.objects.filter(user=_engage.user)
                for infor in _infor:
                    _person_list.append([_engage.user, infor])
    
            _comments_person_list = set()
            _comments_users = Comments.objects.filter(event=_event).order_by('-comments_time').select_related('user')
            for _users in _comments_users:
                #user=Users.objects.filter()
                _comments_person_list.add(_users.user)
            
            _comments_users_list=[]
        
            for _person in _comments_person_list:
                infor = UserProfile.objects.get(user=_person)
                _comments=Comments.objects.filter(user=_person, event=_event).order_by('-comments_time')
                _comments_users_list.append([_person,_comments,infor.make_public_your_user_name])
        
            return render(request, 'events/detail.html', {'indate_':indate, 'comments_person_list_':_comments_person_list, 'comments_users_list':_comments_users_list,'is_full_':_is_full, 'is_engage_': _is_engage, 'is_favorite_': _is_favorite, 'person_list_': _person_list, 'event1': event1}, context)

@login_required
def engage(request, event_id):
    _event = get_object_or_404(Events, pk=event_id)
    _user = request.user
    if _event.engaged_people == _event.capacity:
        messages.success(request, "Join fails.")
        return HttpResponseRedirect(reverse('events:detail', args=(_event.id,)))
    else:
        _event.engaged_people += 1
        _event.save()
        if Engagement.objects.filter(user=_user, event=_event).count() == 0:
            Engagement.objects.create(user=_user, event=_event, engage_time=timezone.now(), is_engage=True)
            from_zone = tz.gettz('UTC')
            to_zone = tz.gettz('America/Vancouver')
            _starttime = _event.starttime
            _localtime = _starttime.astimezone(to_zone)
            subject = '[QuickActivity - Do Not Reply] You Have Joined an Activity!'
            message = 'Hi ' + _user.username + ',\n\n' + 'You have successfully joined the activity ' + _event.title +'. The starting time is ' + unicode(_localtime) + ' and the location is ' + _event.location + '.\n\nHave fun!\n\nYours,\nQuickActivity Team\n'
            try:
                send_mail(subject, message, 'cmpt470group6@gmail.com', [_user.email], fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "Join succeeds.")
        else:
			messages.success(request, "Join fails.")
        
    	return HttpResponseRedirect(reverse('events:detail', args=(_event.id,)))

@login_required
def dis_engage(request, event_id):
    _event = get_object_or_404(Events, pk=event_id)
    _user = request.user
    if Engagement.objects.filter(user=_user, event=_event).count() != 0:
        Engagement.objects.get(user=_user, event=_event, is_engage=True).delete()
	_event.engaged_people -= 1
	_event.save()
	subject = '[QuickActivity - Do Not Reply] You Have Canceled an Activity!'
        message = 'Hi ' + _user.username + ',\n\n' + 'You have successfully canceled the activity ' + _event.title + '.\n\nYours,\nQuickActivity Team\n'
        try:
            send_mail(subject, message, 'cmpt470group6@gmail.com', [_user.email], fail_silently=True)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        messages.success(request, "Cancel join succeeds.")
    else:
        messages.success(request, "Cancel join fails")
    return HttpResponseRedirect(reverse('events:detail', args=(_event.id,)))

@login_required
def favorite(request, event_id):
    _event = get_object_or_404(Events, pk=event_id)
    _user = request.user
    if Bookmark.objects.filter(user=_user, event=_event).count() == 0:
        Bookmark.objects.create(user=_user, event=_event, is_favorite=True)
        messages.success(request, "Favorite succeeds.")
    else:
        messages.error(request, "Favorite fails.")
    return HttpResponseRedirect(reverse('events:detail', args=(_event.id,)))

@login_required
def dis_favorite(request, event_id):
    _event = get_object_or_404(Events, pk=event_id)
    _user = request.user
    if Bookmark.objects.filter(user=_user, event=_event).count() != 0:
        Bookmark.objects.get(user=_user, event=_event, is_favorite=True).delete()
        messages.success(request, "Cancel favorite succeeds")
    else:
        messages.error(request, "Cancel favorite fails.")
    return HttpResponseRedirect(reverse('events:detail', args=(_event.id,)))

@login_required
def make_comments(request, event_id):
    _event = get_object_or_404(Events, pk=event_id)
    _user = request.user
    _comments = request.POST['comments']
    Comments.objects.create(user=_user, event=_event, comments=_comments, comments_time=timezone.now())
    return HttpResponseRedirect(reverse('events:detail', args=(_event.id,)))

def smap(request):
    # Since we know the user is logged in, we can now just log them out.
	context = RequestContext(request)
    # Take the user back to the homepage.
	return render_to_response(
            'events/registerdmap.html',
            context)

def cmap(request):
    # Since we know the user is logged in, we can now just log them out.
	context = RequestContext(request)
    # Take the user back to the homepage.
	return render_to_response(
            'events/registermap.html',
            context)

def pdfproduce(request, event_id):

    #grab a event query set
    event = get_object_or_404(Events, pk=event_id)

    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('America/Vancouver')
    _starttime = event.starttime
    _localtime = _starttime.astimezone(to_zone)
    _endtime = event.endtime
    _localtime2 = _endtime.astimezone(to_zone)


    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="%s.pdf"' %(event.title)

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)


    #grab thi ngs we want to put on the pdf output
    date_now = datetime.date.today()
    printdate = "PDF Created Time: " +"%s" %date_now

    e_title = "Title: " +"%s" %(event.title)
    e_brief_intro = "Description: " +"%s" %(event.brief_intro)
    e_organizer = "Organizer: " +"%s" %(event.organizer)
    e_contact_email = "Contact E-mail: " +"%s" %(event.contact_email)
    e_contact_phonenumber = "Contact Phone Number: " +"%s" %(event.contact_phonenumber)
    e_capacity = "Capacity: " +"%s" %(event.capacity)
    e_age_limit = "Age Limit: " +"%s" %(event.age_limit)
    #e_ticket = "Ticket Link: " +"%s" %(event.ticket)
    #e_description = "Ticket Description: " +"%s" %(event.description)
    e_starttime = "Start Time: " +"%s" %(_localtime)
    e_endtime = "End Time: " +"%s" %(_localtime2)
    e_catogory = "Category : " 
    if event.music: 
        e_catogory += "Music "
    if event.sports:
        e_catogory += "Sports"
    if event.food:
        e_catogory += "Food"
    if event.party:
        e_catogory += "Party"
    if event.arts:
        e_catogory += "Arts"
    if event.business:
        e_catogory += "Business"
    e_street_number = "Street Number: " +"%s" %(event.street_number)
    e_street_name = "Street Name: " +"%s" %(event.street_name)
    e_city_name = "City Name: " +"%s" %(event.city_name)
    e_province_name = "Province Name: " +"%s" %(event.province_name)
    e_postal_code= "Postal Code: " +"%s" %(event.postal_code)
    e_country_name = "Country Name: " +"%s" %(event.country_name)
   
    
    #Draw event on the PDF
    #drawPdfHeader(p, printdate, e_title)
    p.setFont("Helvetica-Bold", 30) 
    p.drawCentredString(300, 800, "Activity Detail")
    p.setFont("Helvetica", 16)
    p.drawString(100, 660, "*********************************************************")
    p.drawString(100, 650, printdate)
    p.drawString(100, 625, e_title)
    p.drawString(100, 600, e_brief_intro)
    p.drawString(100, 575, e_organizer)
    p.drawString(100, 550, e_contact_email)
    p.drawString(100, 525, e_contact_phonenumber)
    p.drawString(100, 500, e_capacity)
    p.drawString(100, 475, e_age_limit)
    #p.drawString(100, 450, e_ticket)
    #p.drawString(100, 425, e_description)
    p.drawString(100, 450, e_starttime)
    p.drawString(100, 425, e_endtime)
    p.drawString(100, 400, e_catogory)
    p.drawString(100, 375, e_street_number)
    p.drawString(100, 350, e_street_name)
    p.drawString(100, 325, e_city_name)
    p.drawString(100, 300, e_province_name)
    p.drawString(100, 275, e_postal_code)
    p.drawString(100, 250, e_country_name)
    p.drawString(100, 240, "_________________________________________")
    p.drawImage( '/home/group6/finalactivity'+event.poster.url , 225, 687, 150, 100)


    # Close the PDF object cleanly.
    p.showPage()
    p.save()


    #Get the value of the BytesIO buffer and write it to the response.
    pdfcontent = buffer.getvalue()
    buffer.close()
    response.write(pdfcontent)
    return response

def json_detail(request, event_id):
	event_info = {}	
	_event = get_object_or_404(Events, pk=event_id)
	event_info["title"] = _event.title
	event_info["organizer"] = _event.organizer
	event_info["capacity"] = _event.capacity
	event_info["number of participants"] = _event.engaged_people
	event_info["start time in UTC"] = str(_event.starttime)
	event_info["end time in UTC"] = str(_event.endtime)
	event_info["location"] = _event.location
	event_info["ticket link"] = _event.ticket
	event_info["contact email"] = _event.contact_email
	event_info["contact phone"] = _event.contact_phonenumber
	event_info["category isMusic"] = _event.music
	event_info["category isSports"] = _event.sports
	event_info["category isFood"] = _event.food
	event_info["category isParty"] = _event.party
	event_info["category isArts"] = _event.arts
	event_info["category isBusiness"] = _event.business
	event_info["brief introduction"] = _event.brief_intro
	event_info["detailed description"] = _event.description
	event_info["update time in UTC"] = str(_event.updatedate)
	#info = HttpResponse()
	info = HttpResponse(content_type = "application/json")

	info['Content-Disposition'] = 'inline; filename="%s.json"'%(_event.title)
	#info.write(json.dumps(contact_info, sort_keys=True));
	info.write('{\n  "title": ' + json.dumps(event_info["title"]) + ', \n  "organizer": ' + json.dumps(event_info["organizer"]) + ', \n  "capacity": ' + json.dumps(event_info["capacity"]) + ', \n  "number of participants": ' + json.dumps(event_info["number of participants"]) + ', \n  "start time in UTC": ' + json.dumps(event_info["start time in UTC"]) + ', \n  "end time in UTC": ' + json.dumps(event_info["end time in UTC"]) + ', \n  "location": ' + json.dumps(event_info["location"]) + ', \n  "ticket link": ' + json.dumps(event_info["ticket link"]) + ', \n  "contact email": ' + json.dumps(event_info["contact email"]) + ', \n  "contact phone": ' + json.dumps(event_info["contact phone"]) + ', \n  "category isMusic": ' + json.dumps(event_info["category isMusic"]) + ', \n  "category isSports": ' + json.dumps(event_info["category isSports"]) + ', \n  "category isFood": ' + json.dumps(event_info["category isFood"]) + ', \n  "category isParty": ' + json.dumps(event_info["category isParty"]) + ', \n  "category isArts": ' + json.dumps(event_info["category isArts"]) + ', \n  "category isBusiness": ' + json.dumps(event_info["category isBusiness"]) + ', \n  "brief introduction": ' + json.dumps(event_info["brief introduction"]) + ', \n  "detailed description": ' + json.dumps(event_info["detailed description"]) + ', \n  "update time in UTC": ' + json.dumps(event_info["update time in UTC"]) + '\n}\n');
	return info;
