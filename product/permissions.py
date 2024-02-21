from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: 
            return True
        else: # put ,delete ,post
            bool(request.user and request.user.is_staff)
            
            
class ReviewerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view,obj):
        if request.method in permissions.SAFE_METHODS: #get
            return True
        else:
            return obj.user==request.user # 
        
class MyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':  # 'POST' oo use kora jai
            return True
        return False