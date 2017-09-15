from rest_framework import permissions


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has the `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        if request.method == 'OPTIONS' or request.user.is_staff:
            return True

        # Instance must have an attribute named `user`.
        return obj.user == request.user
