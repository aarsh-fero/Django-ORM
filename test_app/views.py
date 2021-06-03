from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, serializers
from django.http import HttpResponse

from .models import Author, Book, Genre, PagesWritten, Publisher, Store
from .serializers import AuthorSerializer, BookSerializer, GenreSerializer, PagesWrittenSerializer, StoreSerializer
from .custom_permissions import CustomPermission

import logging

# Create your views here.

def home(request):
	# logging.debug("DEBUG: In HOME")
	# logging.warning("In HOME")
	l = logging.getLogger("custom_logger")
	l.info("Just some INFO")
	l.warning("Just a warning")
	return HttpResponse("<h1>Home Page</h1>") 


# class MovieViewSet(viewsets.ModelViewSet):
# 	queryset = Movie.objects.all()
# 	serializer_class = MovieSerializer


class StoreViewSet(viewsets.ModelViewSet):

	authentication_classes = [ BasicAuthentication, SessionAuthentication ]

	permission_classes = [ IsAuthenticated ]
	queryset = Store.objects.all()
	serializer_class = StoreSerializer
	
	# null_queryset = Store.objects.none()
	# null_queryset |= queryset # null_queryset = null_queryset + queryset


class BookViewSet(viewsets.ModelViewSet):

	authentication_classes = [ BasicAuthentication, SessionAuthentication ]

	permission_classes = [ IsAuthenticated ]
	queryset = Book.objects.all()
	serializer_class = BookSerializer

	def update(self, request, *args, **kwargs):

		id = kwargs['pk']
		if CustomPermission.has_update_permission(self, request, id) is False:
			raise serializers.ValidationError("Not Authorized to Update")

		return super().update(request, *args, **kwargs)

	def destroy(self, request, *args, **kwargs):

		id = kwargs['pk']
		if CustomPermission.has_delete_permission(self, request, id) is False:
			raise serializers.ValidationError("Not Authorized to Delete")
		
		return super().destroy(request, *args, **kwargs)

class AuthorViewSet(viewsets.ModelViewSet):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer


class PagesWrittenViewSet(viewsets.ModelViewSet):
	queryset = PagesWritten.objects.order_by('book')
	serializer_class = PagesWrittenSerializer


class GenreViewSet(viewsets.ModelViewSet):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer
