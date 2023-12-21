""" from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token=Token.objects.create(user=instance)

        # Create an activation link with the token
        uid = urlsafe_base64_encode(force_bytes(instance.pk))
        activation_url = reverse('activate', kwargs={'uidb64': uid, 'token': token})
        activation_link = f"{settings.BASE_URL}{activation_url}"

        # Send a plain text activation email
        subject = 'Activate Your Account'
        message = f'Thank you for registering. Click the link below to activate your account:\n\n{activation_link}'
        from_email = settings.EMAIL_HOST_USER
        to_email = [instance.email]

        send_mail(subject, message, from_email, to_email) """

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


""" from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse

@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        # Generate an activation token
        token = default_token_generator.make_token(instance)

        # Create an activation link with the token
        uid = urlsafe_base64_encode(force_bytes(instance.pk))
        activation_url = reverse('activate', kwargs={'uidb64': uid, 'token': token})
        activation_link = f"{settings.BASE_URL}{activation_url}"

        # Send an activation email
        subject = 'Activate Your Account'
        message = f'Thank you for registering. Click the link below to activate your account:\n\n{activation_link}'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [instance.email]
        send_mail(subject, message, from_email, to_email) """



""" from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# from django.dispatch import receiver
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from django.db.models.signals import Signal
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        # Generate an activation token
        token = default_token_generator.make_token(instance)

        # Create an activation link with the token
        uid = urlsafe_base64_encode(force_bytes(instance.pk))
        activation_url = reverse('activate', kwargs={'uidb64': uid, 'token': token})
        activation_link = f"{settings.BASE_URL}{activation_url}"

        # Send an activation email
        subject = 'Activate Your Account'
        message = f'Thank you for registering. Click the link below to activate your account:\n\n{activation_link}'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [instance.email]
        send_mail(subject, message, from_email, to_email) """


""" from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        # Generate an activation token
        token = default_token_generator.make_token(instance)

        # Create an activation link with the token
        uid = urlsafe_base64_encode(force_bytes(instance.pk))
        activation_url = reverse('activate', kwargs={'uidb64': uid, 'token': token})
        activation_link = f"{settings.BASE_URL}{activation_url}"

        # Send an activation email
        subject = 'Activate Your Account'
        message = f'Thank you for registering. Click the link below to activate your account:\n\n{activation_link}'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [instance.email]
        send_mail(subject, message, from_email, to_email)
 """



        
        
        


""" User = get_user_model()

user_registered = Signal()

@receiver(user_registered)
def send_activation_email(sender, user, **kwargs):
    activation_key = get_random_string(32)
    user.activation_key = activation_key
    user.save()

    subject = 'Activate Your Account'
    message = f'Thank you for registering with us. Please click the link below to activate your account:\n\n' \
              f'http://your-frontend-app/activate/{activation_key}/'

    send_mail(subject, message, 'from@example.com', [user.email]) """