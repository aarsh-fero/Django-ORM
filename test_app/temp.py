from .models import *

Author.objects.all().delete()
Book.objects.all().delete()
Publisher.objects.all().delete()
Store.objects.all().delete()


a = Author.objects.all()
b = Book.objects.all()
p = Publisher.objects.all()
pw = PagesWritten.objects.all()
s = Store.objects.all()

a.count()
b.count()
p.count()
pw.count()
s.count()


a1 = Author.objects.create(name="test", age="22")
p6 = Publisher.objects.get(id=6)

# error
bk = Book.objects.create(name="JavaScript", price=300, pages=852, rating=6.9, publisher=p6) 

# success
x = PagesWritten.objects.create(author=a1, book=bk, pages_written=100)

PagesWritten.objects.all()
y = PagesWritten.objects.last()

y.author
y.author.name

y.book
y.book.name
y.book.pages
y.book.price
y.book.rating
y.book.publisher
y.book.publisher.name

 
