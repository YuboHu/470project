from django.shortcuts import render, render_to_response,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User

def cmap(request):
    # Since we know the user is logged in, we can now just log them out.
	context = RequestContext(request)
    # Take the user back to the homepage.
	return render_to_response(
            'map/registermap.html',
            context)