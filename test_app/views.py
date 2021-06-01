from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, serializers
from django.http import HttpResponse

from .models import Author, Book, Genre, PagesWritten
from .serializers import AuthorSerializer, BookSerializer, GenreSerializer, PagesWrittenSerializer
from .permissions import CustomPermission

import logging
# Create your views here.

def home(request):
	# logging.debug("DEBUG: In HOME")
	# logging.warning("In HOME")
	l = logging.getLogger("custom_logger")
	l.info("Just some INFO")
	l.warning("Just a warning")
	return HttpResponse("<h1>Home Page</h1>") 


class StandardResultsSetPagination(PageNumberPagination):
	page_size = 100
	page_size_query_param = 'page_size'
	max_page_size = 1000


class BookViewSet(viewsets.ModelViewSet):

	authentication_classes = [ BasicAuthentication, SessionAuthentication ]

	permission_classes = [ IsAuthenticated ]
	# pagination_class = StandardResultsSetPagination

	queryset = Book.objects.all()
	serializer_class = BookSerializer

	def update(self, request, *args, **kwargs):

		if CustomPermission.has_update_permission(self, request) is False:
			raise serializers.ValidationError("Not Authorized")

		return super().update(request, *args, **kwargs)


class AuthorViewSet(viewsets.ModelViewSet):
	queryset = Author.objects.order_by('name')
	serializer_class = AuthorSerializer


class PagesWrittenViewSet(viewsets.ModelViewSet):
	queryset = PagesWritten.objects.order_by('book')
	serializer_class = PagesWrittenSerializer


class GenreViewSet(viewsets.ModelViewSet):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer
