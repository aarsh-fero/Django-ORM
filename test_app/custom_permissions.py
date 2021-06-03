from rest_framework import permissions
from .models import Book


class CustomPermission(permissions.BasePermission):
	message = "Can't Update Book."

	def has_permission(self, request, view):
		return super().has_permission(request, view)

	def has_update_permission(self, request, id):
		
		b = Book.objects.get(id=id)
		
		if b.added_by == request.user:
			return True
		return False
		
		# book_name = request.data['name']
		# b = Book.objects.get(name=book_name)
		
		# if b.added_by == request.user:
		# 	return True
		# return False

	def has_delete_permission(self, request, id):
		b = Book.objects.get(id=id)
		# print(request.user)
		# print(b)
		# print(b.author.all())
		# print(b.added_by)
		
		if b.added_by == request.user:
			return True
		return False