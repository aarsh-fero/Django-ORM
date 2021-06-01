from django.contrib.auth.models import User
from django.db.models.aggregates import Sum
from rest_framework import serializers

from .models import Author, Book, Genre, PagesWritten

class AuthorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Author
		fields = ('name', 'age')


class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = "__all__"


class BookSerializer(serializers.ModelSerializer):

	genre = GenreSerializer(many=True)
	# genre = serializers.ReadOnlyField(source='genre.name')
	# genre = serializers.SlugRelatedField(slug_field="genre.name", read_only=True)

	class Meta:
		model = Book
		fields = ('id', 'name', 'price', 'pages', 'rating', 'publisher', 'genre', 'added_by', 'updated_by')
		read_only_fields = ['id', 'added_by', 'updated_by']

	def create(self, validated_data):
		print(validated_data)
		# try:
		# 	user = self.context.get('request').user
		# 	print(user)
		# 	print(user.is_anonymous)
		# 	if not user.is_anonymous:
		# 		print("AUTHORIZED")
		# 		validated_data['added_by'] = user
		# 	else:
		# 		print("NOT AUTHORIZED")
		# 		raise serializers.ValidationError("NOT AUTHORIZED")
		# except:
		# 	raise serializers.ValidationError("NOT AUTHORIZED")
		
		user = self.context.get('request').user
		validated_data['added_by'] = user
		return super().create(validated_data)


	def update(self, instance, validated_data):
		try:
			user = self.context.get('request').user
			if not user.is_anonymous:
				print("NOT AUTHORIZED")
				validated_data['updated_by'] = user
			else:
				print("NOT AUTHORIZED")
				raise serializers.ValidationError("NOT AUTHORIZED")
		except:
			print("NOT AUTHORIZED")
			raise serializers.ValidationError("NOT AUTHORIZED")

		return super().update(instance, validated_data)


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