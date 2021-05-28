from django.core.management.base import BaseCommand
from ...models import Author, Book, PagesWritten, Publisher, Store

import random

import requests

class Command(BaseCommand):
	# This command is for inserting Publisher, Book, Store into database.
	# Insert 10 Publishers, 200 Books, 20 Stores.

	locations = ['Ahmedabad', 'Mumbai', 'Delhi', 'Kolkata', 'Chennai', 'Banglore', 'Pune', 'Hyderabad', 'Jaipur', 'Jodhpur']

	def delete_old_data(self):
		print("DELETING OLD DATA...")
		Author.objects.all().delete()
		Book.objects.all().delete()
		PagesWritten.objects.all().delete()
		Publisher.objects.all().delete()
		Store.objects.all().delete()
		print("DELETED OLD DATA...")


	def create_publishers(self, num):
		print("CREATING Publishers...")

		# create 10 publishers
		publishers = [
			Publisher(name=f"Publisher{index}", location=f"{self.locations[random.randint(0, len(self.locations) - 1)]}") for index in range(1, num + 1)
		]
		Publisher.objects.bulk_create(publishers)

		print("Publishers CREATED...")


	def create_authors(self, num_authors=50):
		print("CREATING AUTHORS")

		getUserURL = "https://api.randomuser.me"

		for i in range(num_authors):
			user = requests.get(getUserURL).json()['results'][0]
			author_name = f"{user['name']['first']} {user['name']['last']}"
			author_age = f"{user['dob']['age']}"
			author = Author.objects.create(name=author_name, age=author_age)
			author.save()
		# Author.objects.bulk_create(authors)

		print("AUTHORS CREATED")


	def create_books(self):
		print("CREATING BOOKS...")

		# create 20 books for every publishers
		# all_authors = Author.objects.all()
		
		counter = 0
		# books = []
		for publisher in Publisher.objects.all():
			for _ in range(20):
				counter += 1
				book = Book.objects.create(
					name=f"Book{counter}",
					price=random.randint(500, 3000),
					pages=random.randint(100, 10000),
					rating=round(random.random(), 2) * 10,
					publisher=publisher
				)
				book.save()
				# for _ in range(random.randint(1, 4)):
				# 	book.author.add(Author.objects.get(id=random.randint(1, 50)))

		print("BOOKS CREATED...")


	def create_stores(self):
		print("CREATING STORES...")

		# create 20 stores and insert 10 books in every store
		books = list(Book.objects.all())
		for i in range(20):
			temp_books = [books.pop(0) for i in range(10)]
			store = Store.objects.create(
				name=f"Store{i+1}",
				location=f"{self.locations[random.randint(0, len(self.locations) - 1)]}"
			)
			store.books.set(temp_books)
			store.save()

		print("STORES CREATED...")


	def create_through_pages_written(self):

		pages_written_bulk = list()
		for i in range(20):
			
			author = Author.objects.get(id=i)
			book = Book.objects.get(id=i)
			pages_written = random.randint(50, 500)
			pages_written_bulk.append(PagesWritten(author=author, book=book, pages_written=pages_written))
		
		PagesWritten.objects.bulk_create(pages_written_bulk)


	def handle(self, *args, **options):

		print("INSERTING QUERIES...")

		# self.delete_old_data()

		# self.create_publishers(10)

		# self.create_authors(50)

		# self.create_books()

		self.create_stores()

		# self.create_through_pages_written()