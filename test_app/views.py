from django.shortcuts import render
from django.http import HttpResponse

import logging
# Create your views here.

def home(request):
	# logging.debug("DEBUG: In HOME")
	# logging.warning("In HOME")
	l = logging.getLogger("custom_logger")
	l.info("Just some INFO")
	l.warning("Just a warning")
	return HttpResponse("<h1>Home Page</h1>") 