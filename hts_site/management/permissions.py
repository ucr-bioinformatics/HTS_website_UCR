from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has the `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        if request.method == 'OPTIONS' or request.user.is_staff:
            return True

        # Instance must have an attribute named `user`.
        return obj.user == request.user


class IsProjectOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'OPTIONS' or request.user.is_staff:
            return True

        return obj.project.user == request.user
