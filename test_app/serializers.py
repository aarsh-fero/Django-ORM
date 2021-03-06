from django.db.models.aggregates import Count, Sum
from rest_framework import serializers

from .models import Author, Book, PagesWritten


class AuthorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Author
		fields = ('name', 'age')


class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('id', 'name', 'price', 'pages', 'rating')


class PagesWrittenSerializer(serializers.ModelSerializer):
	class Meta:
		model = PagesWritten
		fields = ('author', 'book', 'pages_written')

	
	def validate(self, data):

		# ------------------------------------------------------------
		# t = PagesWritten.objects.filter(book=data['book']).annotate(Count('pages_written')).aggregate(total_pages_written=Sum('pages_written'))
		# print(f'Total Pages Written: {t["total_pages_written"]}')
		# ------------------------------------------------------------
		
		# t = PagesWritten.objects.filter(book=data['book']).annotate(total_pages_written=Count('pages_written')).aggregate(Sum('pages_written'))
		# t = PagesWritten.objects.filter(book=data['book']).aggregate(total_authors=Count('pages_written'))
		
		pw = PagesWritten.objects.select_related('book').filter(author=data['author'], book=data['book']).first()
		if pw is not None:
			raise serializers.ValidationError("Can't add same author again")


		# t = PagesWritten.objects.filter(book=data['book']).annotate(Count('pages_written'), filter=	).aggregate(total_pages_written=Sum('pages_written'))
		# print(f'Total Pages Written: {t["total_pages_written"]}')

		total = Book.objects.prefetch_related('books_written').annotate(page_count=Sum('books_written__pages_written')).last().page_count


		b = Book.objects.filter(name=data['book']).first()
		print(f'Total Pages in Book: {b.pages}')
		if b is not None:
			pages = data['pages_written']
			# if pages + total > b.pages:
			if pages + total > b.pages:
				raise serializers.ValidationError("Pages written must be less than pages of book")
			return data

		raise serializers.ValidationError("Book Not Found")