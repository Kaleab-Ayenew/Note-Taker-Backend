from rest_framework.permissions import BasePermission, IsAuthenticated

class OwnsThisObject(BasePermission):

    message = "You don't have permission to acess this data."

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.user == obj.owner
        
class IsAuthAndOwnsObject(IsAuthenticated): #Extends the IsAuthenticated permission class to enable object level permission checking

    message = "You don't have permission to acess this data."

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.user == obj.owner