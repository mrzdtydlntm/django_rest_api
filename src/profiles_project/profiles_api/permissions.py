"""
uses to determine if the user has the permission
to make change they're asking (legal permission checking)
"""

from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    #allow user to edit their own profiles
    def has_object_permission(self, request, view, obj):
        #check user is trying to edit their own profile
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
        #checking that the object the user is trying to check has the
        #same id of the user that's currently authenticated in the system
    