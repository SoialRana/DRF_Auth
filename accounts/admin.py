from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
# admin.site.register(User)

# @admin.register(User)   # when we write this line then last line not required
class AccountAdmin(UserAdmin):
    # Model Field Names.....They will be displayed as columns in the admin list view.
    list_display = ('id','email', 'first_name', 'last_name','is_active') # list_display can be list or tuple
    # list_display = ('email', 'first_name', 'last_name', 'username', 'updated_at', 'created_at', 'is_active') # list_display can be list or tuple
 
    # def custom_active_status(self,obj):
    #     if obj.is_active:
    #         return "Active User"
    #     return "Inactive User"
    # custom_active_status.short_description = 'Active Status'
    # list_display = ['email', 'first_name', 'last_name','username','full_name','custom_active_status']
    
    
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