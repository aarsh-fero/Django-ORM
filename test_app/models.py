# from django.contrib.auth
from django.contrib.auth.models import User
from django.db import models
from rest_framework import generics

# Create your models here.

LOCATIONS = (
		('Ahmedabad', 'Ahmedabad'),
		('Mumbai', 'Mumbai'),
		('Delhi', 'Delhi'),
		('Kolkata', 'Kolkata'),
		('Chennai', 'Chennai'),
		('Banglore', 'Banglore'),
		('Pune', 'Pune'),
		('Hyderabad', 'Hyderabad'),
		('Jaipur', 'Jaipur'),
		('Jodhpur', 'Jodhpur'),
	)


class Genre(models.Model):
	name = models.CharField(max_length=25, unique=True)

	def __str__(self) -> str:
		return self.name	


class Author(models.Model):
	author = models.OneToOneField(User, on_delete=models.CASCADE)
	# name = models.CharField(max_length=100)
	age = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.author.username
		# return self.name


class Publisher(models.Model):
	
	name = models.CharField(max_length=255)

	location = models.CharField(max_length=25, choices=LOCATIONS)

	def __str__(self):
		return self.name

	
class Book(models.Model):
	name = models.CharField(max_length=255, unique=True)
	price = models.IntegerField(null=False, blank=False)
	pages = models.IntegerField(null=False, blank=False)
	rating = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
	authors = models.ManyToManyField(Author, related_name="book_author")#, through='PagesWritten')
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	genre = models.ManyToManyField(Genre, related_name="book_genre")
	added_by = models.ForeignKey(User, related_name="books_added", on_delete=models.SET_NULL, null=True, blank=True)
	updated_by = models.ForeignKey(User, related_name="books_updated", on_delete=models.SET_NULL, null=True, blank=True)

	class Meta:
		default_related_name = 'books'

	def __str__(self):
		return self.name


class Store(models.Model):

	name = models.CharField(max_length=255)
	books = models.ManyToManyField(Book)
	location = models.CharField(max_length=25, choices=LOCATIONS)

	class Meta:
		default_related_name = 'stores'

	def __str__(self):
		return self.name


class PagesWritten(models.Model):
	author = models.ForeignKey('Author', related_name='author_wrote', on_delete=models.CASCADE, null=True)
	book = models.ForeignKey('Book', related_name='books_written', on_delete=models.CASCADE, null=True, blank=True)
	pages_written = models.IntegerField()

	def __str__(self) -> str:
		return f"{self.author}: {self.book}"


# class BookGenre(models.Model):
# 	genre = models.ForeignKey(Genre, on_delete=CASCADE)
# 	book = models.ForeignKey(Book, on_delete=CASCADE)


# ========================================================================================================

'''

OTT_PLATFORMS = (
	('Netflix', 'Netflix'),
	('Amazon Prime', 'Amazon Prime'),
	('HotStar', 'HotStar'),
	('YouTube', 'YouTube'),
	('Zee5', 'Zee5'),
	('Voot', 'Voot'),
	('MX Player', 'MX Player'),
)

MOVIES_GENRE = (
	('Action', 'Action'),
	('Sci-Fi', 'Sci-Fi'),
	('Romantic', 'Romantic'),
	('Animated', 'Animated'),
	('Horror', 'Horror'),
	('Thriller', 'Thriller'),
	('Comedy', 'Comedy'),
	('Kids', 'Kids'),
)


class Actor(models.Model):
	
	GENDER = (
		('m', 'Male'),
		('f', 'Female')
	)
	actor = models.OneToOneField(User, on_delete=models.CASCADE)
	gender = models.CharField()
	age = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.name


class Director(models.Model):
	name = models.CharField(max_length=255, )
	age = models.PositiveSmallIntegerField()


class Platform(models.Model):

	SUBSCRIPTION_TYPE = (
		('Monthly', 'Monthly'),
		('Yearly', 'Yearly'),
	)
	
	name = models.CharField(max_length=255, )
	subscription_type = models.CharField(choices=SUBSCRIPTION_TYPE)
	subscription_price = models.PositiveSmallIntegerField()


class Movie(models.Model):
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField(max_length=255)
	length = models.PositiveSmallIntegerField(verbose_name="Length in Minutes", null=False, blank=False)
	rating = models.IntegerField(blank=True, null=True, max_length=2)
	actors = models.ManyToManyField(Actor, related_name="movie_actors")
	director = models.ForeignKey(Director, on_delete=models.CASCADE)
	genre = models.CharField(choices=MOVIES_GENRE)
	available_on = models.ForeignKey(Platform, related_name="movies_available_on")
	released = models.DateField()
	# added_by = models.ForeignKey(Actor, related_name="movies_added", on_delete=models.SET_NULL, null=True, blank=True)
	# updated_by = models.ForeignKey(Actor, related_name="movies_updated", on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.name
'''