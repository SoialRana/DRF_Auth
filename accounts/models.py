from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,email, password=None,**extra_fields):
        # create and return a regular user(or save a user) with an email and password 
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            # email = self.normalize_email(email), # Normalize the email to a consistent format (lowercase)
            email=email,
            **extra_fields
        ) # create a new user instance ...the user model is created using self.model which refers to custom user model 

        user.set_password(password) # set the password for the user (hash version) ..set_password method is used to hash the password before storing it 
        user.save(using=self._db) # save the user to the database 
        return user

    def create_superuser(self, email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        # Ensure is_superuser and is_staff are True for superuse
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        
        # Create a new superuser
        user = self.create_user(
            email,password,**extra_fields
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    #TODO this should be rename to USER 
    email           = models.EmailField(max_length=100, unique=True)
    first_name      = models.CharField(max_length=50,blank=True)
    last_name       = models.CharField(max_length=50,blank=True)
    # required
    created_at     = models.DateTimeField(auto_now_add=True)
    # created_at     = models.DateTimeField(default=timezone.now())
    updated_at      = models.DateTimeField(auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False) #Determines if the user can access the admin interface.
    is_active       = models.BooleanField(default=True) #Determines if the user account is active.
    # is_active       = models.BooleanField(default=False) #Determines if the user account is active.
    is_superadmin   = models.BooleanField(default=False)

    # Specify the custom user manager
    objects = MyAccountManager() # objects = MyAccountManager(): This sets MyAccountManager as the manager for this model. This means all interactions with the User model (such as creating users or querying users) will be handled by MyAccountManager.
    # username=None
    USERNAME_FIELD = 'email' # This specifies the field to be used for login... use email to login instead of username 
    # REQUIRED_FIELDS = ['username', 'first_name', 'last_name'] # This is a list of fields that required when creating a superuser (besides the username_field) list any required fields besides 'email
    REQUIRED_FIELDS = [] # This is a list of fields that required when creating a superuser (besides the username_field) list any required fields besides 'email
    
    def full_name(self): 
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return str(self.id)+"-"+ self.email     # This method defines how the object should be represented as a string. In this case, the user’s email is returned when the object is printed.
    
    def get_email(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # def has_module_perms(self, app_label):
    def has_module_perms(self, app_label):
        return True
    
    # @property
    # def is_staff(self):
    #     return self.is_admin
    
class BlacklistedToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token
    
    
class Student(models.Model):
    name=models.CharField(max_length=255, unique=True),
    roll=models.IntegerField(),
    city=models.CharField(max_length=255),