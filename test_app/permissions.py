from rest_framework import permissions
from .models import Book


class CustomPermission(permissions.BasePermission):
	message = "Can't Update Book ."

	def has_update_permission(self, request):
		# print(f'request: {request}')
		# print(f'user: {request.user}')
		book_name = request.data['name']
		b = Book.objects.get(name=book_name)
		
		if b.added_by == request.user:
			return True
		return False