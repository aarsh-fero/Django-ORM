from django.shortcuts import render
from rest_framework import serializers, viewsets
from django.http import HttpResponse

from .models import Author, Book, PagesWritten
from .serializers import AuthorSerializer, BookSerializer, PagesWrittenSerializer

import logging
# Create your views here.

def home(request):
	# logging.debug("DEBUG: In HOME")
	# logging.warning("In HOME")
	l = logging.getLogger("custom_logger")
	l.info("Just some INFO")
	l.warning("Just a warning")
	return HttpResponse("<h1>Home Page</h1>") 


class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.order_by('price')
	serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
	queryset = Author.objects.order_by('name')
	serializer_class = AuthorSerializer


class PagesWrittenViewSet(viewsets.ModelViewSet):
	queryset = PagesWritten.objects.order_by('book')
	serializer_class = PagesWrittenSerializer