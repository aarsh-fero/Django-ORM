from django.contrib import admin
from .models import Author, Book, PagesWritten, Publisher, Store

# Register your models here.


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(PagesWritten)
admin.site.register(Publisher)
admin.site.register(Store)