from rest_framework import permissions


class IsRequester(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_requester
