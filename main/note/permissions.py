from rest_framework.permissions import BasePermission

class OwnsThisObject(BasePermission):

    message = "You don't have permission to acess this data."

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif request.user == obj.owner:
            return True
        else:
            return False