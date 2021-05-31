from django.conf.urls import include, url
from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'pages_written', views.PagesWrittenViewSet)

urlpatterns = [
	path('', views.home),
	url(r'^project/', include(router.urls)),
]