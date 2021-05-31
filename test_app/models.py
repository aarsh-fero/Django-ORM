from django.db import models
# Create your models here.


class Author(models.Model):
	name = models.CharField(max_length=100)
	age = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.name

class Publisher(models.Model):
	name = models.CharField(max_length=300)
	location = models.CharField(max_length=25)

	def __str__(self):
		return self.name

	
class Book(models.Model):
	name = models.CharField(max_length=255, unique=True)
	price = models.IntegerField(null=False, blank=False)
	pages = models.IntegerField(null=False, blank=False)
	rating = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
	author = models.ManyToManyField(Author, related_name="author", through='PagesWritten')
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

	class Meta:
		default_related_name = 'books'

	def __str__(self):
		return self.name


class Store(models.Model):
	name = models.CharField(max_length=255)
	books = models.ManyToManyField(Book)
	location = models.CharField(max_length=25)

	class Meta:
		default_related_name = 'stores'

	def __str__(self):
		return self.name


class PagesWritten(models.Model):
	author = models.ForeignKey('Author', related_name='author_wrote', on_delete=models.SET_NULL, null=True)
	book = models.ForeignKey('Book', related_name='books_written', on_delete=models.SET_NULL, null=True, blank=True)
	pages_written = models.IntegerField()

	def __str__(self) -> str:
		return f"{self.author}: {self.book}"