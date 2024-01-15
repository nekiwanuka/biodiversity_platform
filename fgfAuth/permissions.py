from rest_framework import permissions

class AllowAnonymousPost(permissions.BasePermission):
    """
    Custom permission to allow POST requests for anonymous users.
    """
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return False

class IsAdminOrMasterOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow read-only permissions for any request,
    and all actions for admin and master users.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and (request.user.is_staff or (hasattr(request.user, 'master') and request.user.master))

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and (request.user.is_staff or (hasattr(request.user, 'master') and request.user.master))

class IsAdminOrContributorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow read-only permissions for any request,
    and create permissions for contributors.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and hasattr(request.user, 'contributor')

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and hasattr(request.user, 'contributor')
