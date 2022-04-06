from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        else:
            return False


class IsGetOrPostOrPut(BasePermission):
    def has_permission(self, request, view):
        allowed_method = ['GET', 'POST', 'PUT', 'DELETE']
        if request.method in allowed_method:
            return True
        else:
            return False


class IsUserOnly(BasePermission):
    def has_permission(self, request, view):
        allowed_method = ['GET', 'POST', 'PUT', 'DELETE']
        if request.method in allowed_method:
            return True
        else:
            return False


class UserAdminchecks(BasePermission):

    def has_permission(self, request, view):

        allowed_method = ['GET', 'POST', 'PUT', 'DELETE']

        if request.user.is_superuser:
            if request.method in allowed_method:
                return True
            else:
                return False

        else:
            return False


class AuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated :
            return True

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False


class AuthorAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated or request.user.is_superuser:
            return True

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user or request.user.is_superuser:
            return True
        return False
