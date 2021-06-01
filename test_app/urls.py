from django.conf.urls import include, url
from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'pw', views.PagesWrittenViewSet)
router.register(r'genre', views.GenreViewSet)

urlpatterns = [
	path('', views.home),
	path('auth/', include('rest_framework.urls')),
    # path('register/', RegisterUser.as_view(), name="register"),

	url(r'^api/', include(router.urls)),
]