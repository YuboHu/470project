from django.shortcuts import render, render_to_response,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from events.models import Events, EventsCreater,Engagement, Bookmark
from events.forms import EventsForm
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.
def post(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    user=request.user
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    posted = False

    if request.method == 'POST':
       
	events_form = EventsForm(data=request.POST)

        # If the two forms are valid...
        if events_form.is_valid():
            # Save the user's form data to the database.
            event = events_form.save()
	    if 'poster' in request.FILES:
                event.poster = request.FILES['poster']
	    event.pubdate= timezone.now()
	    
	    event.street_number = request.POST['street_number_']
	    event.street_name = request.POST['street_name_']
	    event.city_name = request.POST['city_name_']
	    event.province_name = request.POST['province_name_']
	    event.postal_code = request.POST['postal_code_']
	    event.country_name = request.POST['country_name_']
	    event.latitude = request.POST['latitude_']
	    event.longitude = request.POST['longitude_']
	    
	    
	    event.save()
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            
	    #user = get_object_or_404(UserProfile, pk=user.user_id)
	    EventsCreater.objects.create(events=event,creater=user)
            # Update our variable to tell the template registration was successful.
            posted = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print events_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        events_form = EventsForm()

    # Render the template depending on the context.
    return render_to_response(
            'events/post.html',
            {'events_form': events_form,'posted': posted}, context)

def detail(request, event_id):
    event1 = get_object_or_404(Events, pk=event_id)
    

    context = RequestContext(request)

    _event = get_object_or_404(Events, pk=event_id)
    _user = request.user
    if Engagement.objects.filter(user=_user, event=_event).count() == 0:
        _is_engage = False
    else:
        _is_engage = True

    if Bookmark.objects.filter(user=_user, event=_event).count() == 0:
        _is_favorite = False
    else:
        _is_favorite = True

    #if Engagement.objects.filter(event=_event).count() == 0:
    #    _is_anyone_engage = False
    #    engage_list = 0
    #else:
    #    _is_anyone_engage = True
    _person_list = set()
    _engage_list = Engagement.objects.filter(event=_event).order_by('-engage_time').select_related('user')[:20]
    for _engage in _engage_list:
        _person_list.add(_engage.user)

    return render(request, 'events/detail.html', {'is_engage_': _is_engage, 'is_favorite_': _is_favorite, 'person_list_': _person_list, 'event1': event1}, context)

def engage(request, event_id):
    _event = get_object_or_404(Events, pk=event_id)
    _user = request.user
    if Engagement.objects.filter(user=_user, event=_event).count() == 0:
        Engagement.objects.create(user=_user, event=_event, engage_time=timezone.now(), is_engage=True)
    return HttpResponseRedirect(reverse('events:detail', args=(_event.id,)))

def dis_engage(request, event_id):
    _event = get_object_or_404(Events, pk=event_id)
    _user = request.user
    if Engagement.objects.filter(user=_user, event=_event).count() != 0:
        Engagement.objects.get(user=_user, event=_event, is_engage=True).delete()   
    return HttpResponseRedirect(reverse('events:detail', args=(_event.id,)))

def favorite(request, event_id):
    _event = get_object_or_404(Events, pk=event_id)
    _user = request.user
    if Bookmark.objects.filter(user=_user, event=_event).count() == 0:
        Bookmark.objects.create(user=_user, event=_event, is_favorite=True)
    return HttpResponseRedirect(reverse('events:detail', args=(_event.id,)))

def dis_favorite(request, event_id):
    _event = get_object_or_404(Events, pk=event_id)
    _user = request.user
    if Bookmark.objects.filter(user=_user, event=_event).count() != 0:
        Bookmark.objects.get(user=_user, event=_event, is_favorite=True).delete()
    return HttpResponseRedirect(reverse('events:detail', args=(_event.id,)))

def cmap(request):
    # Since we know the user is logged in, we can now just log them out.
	context = RequestContext(request)
    # Take the user back to the homepage.
	return render_to_response(
            'events/registermap.html',
            context)
