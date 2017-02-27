import csv
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils import timezone
import datetime
from django.db.models import F
from dateutil import tz
from users.forms import UserForm, UserProfileForm, Advan_UserForm
from users.models import UserProfile
from events.models import Engagement, Bookmark, EventsCreater, Events
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def regist(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registeration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # Thi s delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            # Did the user provide a profile a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            #if 'picture' in request.FILES:
            #   profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True
            messages.warning(request, "You have successfully created an account!")
            subject = '[QuickActivity - Do Not Reply] You Have Created an Account!'
	    message = 'Hi ' + user.username + ',\n\n' + 'You have successfully created an account on the QuickActivity website' + '.\n\nYours,\nQuickActivity Team\n'

	    try:
                send_mail(subject, message, 'cmpt470group6@gmail.com', [user.email], fail_silently=True)
	    except BadHeaderError:
                return HttpResponse('Invalid header found.')
        # Invalid form or forms - mistakes or somethi ng else?
        # Print problems to the terminal.
        # They'll also be shown to the user.

        else:
            messages.info(request, user_form.errors)
            messages.info(request, profile_form.errors)
            print user_form.errors, profile_form.errors

        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.

    # Render the template depending on the context.
        return HttpResponseRedirect(reverse('users:index'))

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # Thi s information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machi nery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matchi ng credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect(reverse('users:index'))
            else:
                # An inactive account was used - no logging in!
                messages.error(request, "our account is disabled.")
                return HttpResponseRedirect(reverse('users:index'))
        else:
            messages.error(request, "Invalid login details are supplied.")
            return HttpResponseRedirect(reverse('users:index'))

    # The request is not a HTTP POST, so display the login form.
    # Thi s scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return HttpResponseRedirect(reverse('users:index'))

def index(request):
    context = RequestContext(request)
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
    now=timezone.now()
    eventlatest=list()
    eventpopular=list()
    eventexpire=list()
    start=timezone.now() + datetime.timedelta(days=30)
    if Events.objects.filter(starttime__lt=start).filter(starttime__gt=now).filter(age_limit__lte=age).count()!=0:
	   eventlatest=Events.objects.filter(starttime__lt=start).filter(starttime__gt=now).filter(age_limit__lte=age).order_by('-pubdate')[0]
	   eventpopular=Events.objects.filter(starttime__lt=start).filter(starttime__gt=now).filter(age_limit__lte=age).order_by('-engaged_people')[0]
	   eventexpire= Events.objects.filter(starttime__lt=start).filter(starttime__gt=now).filter(age_limit__lte=age).order_by('starttime')[0]
    return render_to_response(
            'users/home.html',{'eventlatest':eventlatest, 'eventpopular':eventpopular, 'eventexpire':eventexpire},
            context)


@login_required
def homepage(request):
    context = RequestContext(request)
    user=request.user
    userprofile=UserProfile.objects.get(user=user)
    today=datetime.date.today()
    #eventspub_list= EventsPubdate.objects.select_related('events')
    #for e in EventsPubdate.objects.order_by('pubdate').select_related('events'):
    #   events_list.append(e.events)
    #print(events_list)
    #time=0
    if user.is_active:
        age=today.year-userprofile.birthday.year
        m=today.month-userprofile.birthday.month
        if today.day-userprofile.birthday.day<0:
            m-=1
        if m<0:
            age-=1
    else:
        age=16

    recommend_events_list=list()
    events_list = Events.objects.filter(starttime__gt=timezone.now()).filter(age_limit__lte=age).filter(engaged_people__lt=F('capacity')).order_by('engaged_people')
    if userprofile.isMusic:
        for e in events_list:
            if e.music==True:
                recommend_events_list.append(e)
    if userprofile.isSports:
        for e in events_list:
            if e.sports==True:
                recommend_events_list.append(e)
    if userprofile.isFood_Drink:
        for e in events_list:
            if e.food==True:
                recommend_events_list.append(e)
    if userprofile.isParties:
        for e in events_list:
            if e.party==True:
                recommend_events_list.append(e)
    if userprofile.isArts:
        for e in events_list:
            if e.arts==True:
                recommend_events_list.append(e)
    if userprofile.isBusiness:
        for e in events_list:
            if e.business==True:
                recommend_events_list.append(e)
    if len(recommend_events_list)==0:
        recommend_events_list=events_list[:5]
    else:
       recommend_events_list=recommend_events_list[:5]


    week_events_list = list()
    start=timezone.now() + datetime.timedelta(days=7)
    engage_list= Engagement.objects.filter(user=user).filter(is_engage=True)
    for engage in engage_list:
        if engage.event.starttime<start:
            week_events_list.append(engage.event)
    week_events_list.sort()
    return render_to_response(
            'users/homepage.html',{'recommend_events_list':recommend_events_list,'week_events_list':week_events_list},
            context)


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    context = RequestContext(request)
    logout(request)

    # Take the user back to the homepage.
    #render_to_response('users/login.html', {}, context)
    #return render_to_response('users/index.html', {}, context)
    return HttpResponseRedirect(reverse('users:index'))

@login_required
def detail(request):
    #context = RequestContext(request)
    user=request.user
    userprofile = get_object_or_404(UserProfile, user_id=user.id)

    return render(request, 'users/detail.html', {'userprofile': userprofile, 'user': user})
    #context = RequestContext(request)
    #return render_to_response('users/detail.html', {'userprofile': userprofile}, context)


@login_required
def user_profile(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    user=request.user
    userprofile = get_object_or_404(UserProfile, user_id=user.id)

    edited = False

    if request.method == 'POST':
        # Gather the username and password provided by the user.
        #user.username = request.POST['username']
        user.email = request.POST['email_']
        userprofile.birthday = request.POST['birthday_']


        enabled = bool(request.POST.get('make_public_your_user_name'))
        userprofile.make_public_your_user_name = enabled

        userprofile.street_number = request.POST['street_number_']
        userprofile.street_name = request.POST['street_name_']
        userprofile.city_name = request.POST['city_name_']
        userprofile.province_name = request.POST['province_name_']
        userprofile.postal_code = request.POST['postal_code_']
        userprofile.country_name = request.POST['country_name_']
        userprofile.latitude = request.POST['latitude_']
        userprofile.longitude = request.POST['longitude_']

        enabledmusic = bool(request.POST.get('isMusic'))
        userprofile.isMusic = enabledmusic

        enabledsports = bool(request.POST.get('isSports_'))
        userprofile.isSports = enabledsports

        enabledfood = bool(request.POST.get('isFood_Drink_'))
        userprofile.isFood_Drink = enabledfood

        enabledparties = bool(request.POST.get('isParties_'))
        userprofile.isParties = enabledparties

        enabledarts = bool(request.POST.get('isArts_'))
        userprofile.isArts = enabledarts

        enablebus = bool(request.POST.get('isBusiness_'))
        userprofile.isBusiness = enablebus

        userprofile.phonenumber = request.POST['phonenumber_']
        #userprofile.gender = request.POST['gender']
        
        if request.POST.get('sex') == 'male':
            userprofile.isMale = True
            userprofile.isFemale= False
        #enablefemale = bool(request.POST('sex_'))
        else:
            userprofile.isMale = False
            userprofile.isFemale = True

        #$userprofile.gender = self.get_gender_display()
        
        user.save()
        userprofile.save()
        edited = True

    return render_to_response('users/user_profile.html', {'user': user, 'userprofile': userprofile, 'edited': edited}, context)

@login_required
def chapass(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)
    user = request.user

    changed = False
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # Thi s information is obtained from the login form.
        original_password = request.POST['original_password']
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        # Use Django's machi nery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=user.username, password=original_password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matchi ng credentials was found.
        if user:
            if user.is_active:
                if new_password!=confirm_new_password:
                    messages.error(request, "New Passwords do not match.")
                    return render_to_response('users/chapass.html', {}, context)

                else:
                    #user_updated=User.objects.get(user=user)
                    #user_updated=UserProfile.objects.get(user=user)
                    changed = True

                    user.password=new_password
                    user.set_password(user.password)
                    user.save()
		    subject = '[QuickActivity - Do Not Reply] You Have Changed your Password!'
                    message = 'Hi ' + user.username + ',\n\n' + 'You have successfully changed your password' + '.\n\nYours,\nQuickActivity Team\n'
                    try:
                        send_mail(subject, message, 'cmpt470group6@gmail.com', [user.email], fail_silently=True)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')

                    return render_to_response('users/chapass.html', {'changed': changed}, context)

                    #return HttpResponse("Password is changed.")
            else:
                # An inactive account was used - no logging in!
                messages.error(request, "Your account is disabled.")
                return render_to_response('users/home.html', {}, context)
        else:
            # Bad login details were provided. So we can't log the user in.
            messages.error(request, "Original password is wrong.")
            return render_to_response('users/chapass.html', {}, context)

    # The request is not a HTTP POST, so display the login form.
    # Thi s scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('users/chapass.html', {}, context)

@login_required
def map(request):
    # Since we know the user is logged in, we can now just log them out.
	context = RequestContext(request)
    # Take the user back to the homepage.
	return render_to_response(
            'users/registermap.html',
            context)

@login_required
def dmap(request):
    # Since we know the user is logged in, we can now just log them out.
	context = RequestContext(request)
    # Take the user back to the homepage.
	return render_to_response(
            'users/registerdmap.html',
            context)


@login_required
def engaged(request):
    context = RequestContext(request)
    user=request.user

    events_list = set()
    engage_list= Engagement.objects.filter(user=user).filter(is_engage=True)
    for engage in engage_list:
        events_list.add(engage.event)


    return render_to_response(
            'users/engaged.html',{'events_list':events_list},
            context)
    

@login_required
def engaged2(request):
    context = RequestContext(request)
    user=request.user

    events_list = set()
    engage_list= Engagement.objects.filter(user=user).filter(is_engage=True)
    for engage in engage_list:
        events_list.add(engage.event)


    return render_to_response(
            'users/engaged2.html',{'events_list':events_list},
            context)
    

@login_required
def favorite(request):
    context = RequestContext(request)
    user=request.user

    events_list = list()
    favorite_list= Bookmark.objects.filter(user=user).filter(is_favorite=True)
    for favorite in favorite_list:
        events_list.append(favorite.event)


    return render_to_response(
            'users/bookmark.html',{'events_list':events_list},
            context)


@login_required
def posted(request):
    context = RequestContext(request)
    user=request.user

    events_list = list()
    posted_list= EventsCreater.objects.filter(creater=user).order_by('-createdate')
    for posted in posted_list:
        events_list.append(posted.events)


    return render_to_response(
            'users/posted.html',{'events_list':events_list},
            context)
	

@login_required
def showcsv(request, event_id):
    response = HttpResponse(content_type='text/csv')
    _event = get_object_or_404(Events, pk=event_id)
    response['Content-Disposition'] = 'attachment; filename="%s.csv"' %(_event.title)
    
    _user = request.user
    engage_list = Engagement.objects.filter(event=_event)

    writer = csv.writer(response)
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('America/Vancouver')
    _starttime = _event.starttime
    _localtime = _starttime.astimezone(to_zone)
    _endtime = _event.endtime
    _localtime2 = _endtime.astimezone(to_zone)

    writer.writerow(['event title', _event.title])
    writer.writerow(['contact email', _event.contact_email])
    writer.writerow(['start time', _localtime])
    writer.writerow(['end time', _localtime2])
    writer.writerow(['total participants', len(engage_list)])
    writer.writerow(['Number', 'username', 'email'])
    counter = 0
    for engage in engage_list:
        engage_user = engage.user
        counter = counter + 1
        writer.writerow([counter, engage_user.username, engage_user.email])
#        Engagement.objects.create(user=_user, event=_event, engage_time=timezone.now(), is_engage=True)
    return response

def calendar(request):
    # Since we know the user is logged in, we can now just log them out.
	context = RequestContext(request)
    # Take the user back to the homepage.
	return render_to_response(
            'users/calendar.html',
            context)
