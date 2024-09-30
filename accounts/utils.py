from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes

def send_activation_email(user, request):
    # Generate JWT for email activation
    try:
        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)  # Get access token

        # Prepare the email
        current_site = get_current_site(request)
        mail_subject = 'Activate your account'
        activation_link = f"http://{current_site.domain}/account/activate/{token}/"

        message = f"Hi {user.email},\nClick the link below to activate your account:\n{activation_link}"

        email = EmailMessage(mail_subject, message, to=[user.email])
        email.send()
    except Exception as e:
        # Add error logging for troubleshooting
        print(f"Error sending activation email: {e}")
        raise e
""" import logging

logger = logging.getLogger(__name__)


def get_jwt_for_user(user):
    # Generate JWT tokens explicitly including the user_id in the payload.
    refresh = RefreshToken.for_user(user)
    # The access token will include the user_id by default in simplejwt, but
    # if you want to make sure it does or add additional claims, you can do this:
    refresh['user_id'] = user.id  # Explicitly add user_id to the payload
    return str(refresh.access_token) """

""" def send_activation_email(user, request):
    try:
        # Generate JWT token with user_id included
        # token = get_jwt_for_user(user)

        # Prepare the email
        
        # current_site = get_current_site(request)
        # uidb64 =urlsafe_base64_encode(force_bytes(user.pk))
        # mail_subject = 'Activate your account'
        # activation_link = f"http://{current_site.domain}/activate/{token}/"

        # message = f"Hi {user.email},\nClick the link below to activate your account:\n{activation_link}"

        # email = EmailMessage(mail_subject, message, to=[user.email])
        # email.send()
        
        
        # Get the current domain
        current_site = get_current_site(request)
        activation_link = f'http://{current_site.domain}/activate/{token["access"]}'
        
        # Send activation email
        send_mail(
            'Activate Your Account',
            f'Please click the activation link to activate your account: {activation_link}',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

    except Exception as e:
        logger.error(f"Error sending activation email: {e}") """




""" def send_activation_email(user, request):
    # Generate JWT token with user_id included
    token = get_jwt_for_user(user)

    # Prepare the email
    current_site = get_current_site(request)
    mail_subject = 'Activate your account'
    activation_link = f"http://{current_site.domain}/api/account/activate/{token}/"

    message = f"Hi {user.email},\nClick the link below to activate your account:\n{activation_link}"

    email = EmailMessage(mail_subject, message, to=[user.email])
    email.send()

 """

""" from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings

def send_activation_email(user, request):
    current_site = get_current_site(request)
    mail_subject = 'Activate your account'
    message = render_to_string('account/activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })
    to_email = user.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()
 """

# for django 

""" from django.core.mail import EmailMessage
import os

class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject = data['subject'],
            body = data['body'],
            from_email = os.environ.get('EMAIL_FROM'),
            to = [data['to_email']]
        )
        email.send() """