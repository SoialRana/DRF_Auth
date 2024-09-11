from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

# @admin.register(User)   # eta likhle nicher register ti likha lagbe na 
class AccountAdmin(UserAdmin):
    
    # Model Field Names.....They will be displayed as columns in the admin list view.
    """ list_display = ('email', 'first_name', 'last_name', 'username', 'updated_at', 'created_at', 'is_active')
    list_display = ['email', 'first_name', 'last_name', 'username', 'updated_at', 'created_at', 'is_active'] """
    
    
    # Callable Methods on the Model
    list_display = ['email', 'first_name', 'last_name','full_name','username',]
    
    
    # Properties on the Model
    # You can also use properties, which are similar to methods but are accessed like attributes (without parentheses). Properties allow you to calculate or format data dynamically.
    
    
    """ # Callable function to display a custom active status message
    #Callable functions can be used in admin.py to add custom logic that doesn't necessarily need to reside in the model itself. These functions take an instance of the model as an argument and return a value to be displayed in the admin interface.
    def custom_active_status(obj):
        if obj.is_active:
            return "Active User"
        return "Inactive User"
    custom_active_status.short_description = 'Active Status'
    list_display = ['email', 'first_name', 'last_name','username','custom_active_status']
    # here we can't use full_name . if we use show this error: TypeError: AccountAdmin.custom_active_status() takes 1 positional argument but 2 were given """
    
    
    
    # fieldsets = [
    #     ('User Credentials', {"fields": ["email", "password"]}),
    #     ("Personal info", {"fields": ["username", "first_name"]}),
    #     ("Permissions", {"fields": ["is_admin"]}),
    # ]
    list_display_links = ('email',)
    readonly_fields = ('updated_at', 'created_at')
    ordering = ('-created_at',)
    search_fields = ["email",]
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, AccountAdmin)
# admin.site.unregister(Group) 