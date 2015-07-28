from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from events.models import Engagement, Bookmark, EventsCreater
from users.forms import UserForm, UserProfileForm, Advan_UserForm
from users.models import UserProfile
from django.contrib.auth.models import User

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
            # This delays saving the model until we're ready to avoid integrity problems.
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
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.

        else:
            print user_form.errors, profile_form.errors

        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
        'users/regist.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
        context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/users/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('users/login.html', {}, context)

@login_required
def index(request):
    
	context = RequestContext(request)
	user=request.user

	recommend_events_list = set()
	#posted_list= Events.objects.filter(creater=user)
	#for posted in posted_list:
		#events_list.add(posted.events)


	return render_to_response(
            'users/index.html',{'recommend_events_list':recommend_events_list},
            context)

def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are not logged in.")
    else:
        return HttpResponse("You are logged in.")

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    context = RequestContext(request)
    logout(request)

    # Take the user back to the homepage.
    #render_to_response('users/login.html', {}, context)
    #return render_to_response('users/index.html', {}, context)
    return HttpResponseRedirect('/users/')

@login_required
def detail(request, user_id):
    #context = RequestContext(request)

    userprofile = get_object_or_404(UserProfile, user_id=user_id)

    user = get_object_or_404(User, id=user_id)


    return render(request, 'users/detail.html', {'userprofile': userprofile, 'user': user})
    #context = RequestContext(request)
    #return render_to_response('users/detail.html', {'userprofile': userprofile}, context)


@login_required
def user_profile(request, user_id):
    # Like before, get the request's context.
    context = RequestContext(request)

    userprofile = get_object_or_404(UserProfile, user_id=user_id)

    user = get_object_or_404(User, id=user_id)

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

        enablebus = bool(request.POST.get('isBusniess_'))
        userprofile.isBusniess = enablebus

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
        # This information is obtained from the login form.
        original_password = request.POST['original_password']
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=user.username, password=original_password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            if user.is_active:
                if new_password!=confirm_new_password:
                    return HttpResponse("New Passwords are not same.")
                else:
                    #user_updated=User.objects.get(user=user)
                    #user_updated=UserProfile.objects.get(user=user)
                    changed = True

                    user.password=new_password
                    user.set_password(user.password)
                    user.save()

                    return render_to_response('users/chapass.html', {'changed': changed}, context)

                    #return HttpResponse("Password is changed.")
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            return HttpResponse("password is wrong.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
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
def favorite(request):
	context = RequestContext(request)
	user=request.user

	events_list = set()
	favorite_list= Bookmark.objects.filter(user=user).filter(is_favorite=True)
	for favorite in favorite_list:
		events_list.add(favorite.event)


	return render_to_response(
            'users/engaged.html',{'events_list':events_list},
            context)

@login_required
def posted(request):
	context = RequestContext(request)
	user=request.user

	events_list = set()
	posted_list= EventsCreater.objects.filter(creater=user)
	for posted in posted_list:
		events_list.add(posted.events)


	return render_to_response(
            'users/engaged.html',{'events_list':events_list},
            context)

