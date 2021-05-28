from test_app.models import *

Author.objects.all().delete()
Book.objects.all().delete()
Publisher.objects.all().delete()
Store.objects.all().delete()


a = Author.objects.all()
b = Book.objects.all()
p = Publisher.objects.all()
s = Store.objects.all()

a.count()
b.count()
p.count()
s.count()


a = Author.objects.create(name="test", age="22")
p = Publisher.objects.get(id=6)
b = Book.objects.create(name="JS", price=300, pages=852, rating=6.9, publisher=p)
