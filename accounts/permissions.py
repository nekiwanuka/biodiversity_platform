# permissions.py

from rest_framework import permissions

class IsContributorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Contributors can read (GET) and post, others have read-only access
        return request.method in ['GET', 'POST'] or (request.user.is_authenticated and getattr(request.user, 'contributor', False))

class IsMasteruserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Masterusers can perform CRUD operations, others have read-only access
        return request.method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'] or (request.user.is_authenticated and getattr(request.user, 'masteruser', False))

class IsSuperuserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Superusers have all permissions, others have read-only access
        return request.method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'] or (request.user.is_authenticated and request.user.is_superuser)
