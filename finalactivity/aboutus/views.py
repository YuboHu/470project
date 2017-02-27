from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

# Create your views here.
def aboutus(request):
    # Since we know the user is logged in, we can now just log them out.
	context = RequestContext(request)
    # Take the user back to the homepage.
	return render_to_response(
            'aboutus/aboutus.html',
            context)