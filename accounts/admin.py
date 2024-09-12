from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

# @admin.register(User)   # eta likhle nicher register ti likha lagbe na 
class AccountAdmin(UserAdmin):
    list_display = ('email','id', 'first_name', 'last_name', 'username', 'updated_at', 'created_at', 'is_active')
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