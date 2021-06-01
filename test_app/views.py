from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework import viewsets, serializers
from django.http import HttpResponse

from .models import Author, Book, PagesWritten
from .serializers import AuthorSerializer, BookSerializer, PagesWrittenSerializer
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


class BookViewSet(viewsets.ModelViewSet):

	authentication_classes = [ BasicAuthentication, SessionAuthentication ]

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


# class RegisterUser(generics.GenericAPIView):

# 	# queryset = User.objects.all()
# 	serializer_class = UserSerializer
	
# 	def post(self, request):
# 		user = request.data
		
# 		serializer = self.serializer_class(data=user)
# 		serializer.is_valid(raise_exception=True)
# 		serializer.save()

# 		return Response(serializer.data)
