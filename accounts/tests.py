from django.test import TestCase

# Create your tests here.
""" from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields) """
    
    
    
""" from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _

class CustomUserManager(BaseUserManager):
    use_in_migrations = True
   

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields) """
        
        
        
        
""" from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User

def send_otp_via_email(email):
    subject='Your account verification email'
    otp=random.randint(1000,9999)
    message=f'Your otp is {otp}'
    email_from=settings.EMAIL_HOST
    send_mail(subject, message, email_from,[email])
    user_obj=User.objects.get(email=email)
    user_obj.otp=otp
    user_obj.save() """