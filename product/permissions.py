from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser): # jodi user ta admin or authenticated hoi taile 
    def has_permission(self, request, view): # amader parameter hisebe self and request dite hobe 
        if request.method in permissions.SAFE_METHODS: #save method hocche amake get request dewa karon get request dile amader data gulo edit,delete or hariye jawa setar kono voy nie 
            return True
        else: # put ,delete ,post
            bool(request.user and request.user.is_staff) # jodi user hoi and admin site e se staff ki na jodi hoi taile put,dlete,post egula korte dibo..se authenticated user hoilei hobe na take admin site e staff hote hobe 
            
            
class ReviewerOrReadOnly(permissions.BasePermission): # jodi se reviewer hoi taile se dekhte pabe,edit or delete korte parbe ar jodi reviewer na hoi taile sudhu dekhte pabe 
    def has_object_permission(self, request, view,obj):
        if request.method in permissions.SAFE_METHODS: #get
            return True
        else:
            return obj.user==request.user # amader reviewer user jodi authenticated user same hoi take permission gulo dibo   
        # ekhane review 3 hocche ekta object 