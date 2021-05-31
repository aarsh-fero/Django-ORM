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
		print(data)
		book = data['book']
		bk = Book.objects.prefetch_related('books_written').filter(name=book).first()
		print(f"{bk}")
		print(f"{bk.id}")
		print(bk.pages)
		if bk.books_written is None:
			print("bk.books_written is None")
		else:
			print("bk.books_written is not none")
			print(f"{bk.books_written}")

		pw = PagesWritten.objects.select_related('book').filter(author=data['author'], book=data['book'])
		print(pw)
		# if bk:
		# 	a = data['pages_written']
		# 	if a > bk.pages:
		# 		raise serializers.ValidationE`rror("Pages written must be less than pages of book")
		# 	return data

		raise serializers.ValidationError("Pages written must be less than pages of book")
		# Book.objects.filter()
	
	# def validate_pages_written(self, value):
		# book = self.