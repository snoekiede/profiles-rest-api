from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""
    
    def has_object_permission(self,request,view,obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS: #if request method is in safe methods
            return True #return True
        return obj.id == request.user.id #return True if obj.id is equal