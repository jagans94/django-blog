# First thing import something:
from django.http import HttpResponse # Alloes us to send a response to the user
from django.shortcuts import render  # Allows us to render the html templates in the browser

# Now we need two functions for the two pages we're about to create

# The 'request' object that has info about the user request
def about(request):
	# For now we'll return a simple http response.
	#return HttpResponse('about')
	# Now we're rending the template that need's to be served for a particular request.
	return render(request,'about.html')
# Once the function is ready, hook it up in the urls.py file.

def home(request):
	#return HttpResponse('home')
	return render(request,'home.html')
