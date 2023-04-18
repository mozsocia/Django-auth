from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class IsAdmin(BasePermission):
    """
    Custom permission class to check if a user is an admin.
    """
    message = {'errors': ['User is not a superuser']}

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # # Custom error message complex way
        # if not request.user.is_staff:
        #     raise PermissionDenied(
        #         detail="You must be an admin to access this resource.")

        # Check if the user is an admin
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        return request.user.is_staff
