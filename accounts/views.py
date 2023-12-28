from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistrationSerializer,UserSerializer,LoginSerializer
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from .models import User

# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from .serializers import RegistrationSerializer
from django.contrib.sites.shortcuts import get_current_site

from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from .models import BlacklistedToken
from django.contrib.auth import logout


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            # token, created = Token.objects.get_or_create(user=user)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # USER ACTIVATION
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = f"Click the following link to activate your account: " \
                      f"http://{current_site.domain}/account/activate/{urlsafe_base64_encode(force_bytes(user.pk))}/" \
                      f"{default_token_generator.make_token(user)}/"

            to_email = user.email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            
            return Response({
                # 'access_token': access_token,
                # 'refresh_token': refresh_token,
                'detail': 'Registration successful. Check your email for activation instructions.'
            }, status=status.HTTP_201_CREATED)
            # return Response({'token':token.key,'detail': 'Registration successful. Check your email for activation instructions.'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        # if user is not None:
        #     token, created = Token.objects.get_or_create(user=user)
        #     return Response({'token': token.key, 'user': UserSerializer(user).data}, status=status.HTTP_200_OK)
        # else:
        #     return Response({'detail': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                'access_token': access_token,
                'refresh_token': refresh_token,
                'user': UserSerializer(user).data
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Your account is not activated. Please activate your account from the email'}, status=status.HTTP_401_UNAUTHORIZED)
        
class LoginApi(APIView): #login serializer k validate korbo data k liye 
    def post(self, request):
        try:
            data=request.data
            serializer=LoginSerializer(data=data)
            if serializer.is_valid():
                email=serializer.data['email']
                password=serializer.data['password']
                user = authenticate(request,email=email, password=password)
                
                if user is None:
                    return Response({
                        'status': 401,  # Unauthorized
                        'message': 'Invalid credentials',
                        'data': {}
                    }, status=status.HTTP_401_UNAUTHORIZED)
                    
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)

                return Response({
                    'access_token': access_token,
                    'refresh_token': refresh_token,
                    'user': UserSerializer(user).data
                }, status=status.HTTP_200_OK)
                
            return Response({
                'status': 400,
                'message': 'Validation error',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
            
        except ValidationError as e:
            return Response({
                'status': 400,
                'message': 'Validation error',
                'data': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal server error',
                'data': {}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class LogoutView(APIView):
#     def post(self, request):
#         request.auth.delete()
#         return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        refresh_token = request.data.get('refresh_token')

        if refresh_token:
            BlacklistedToken.objects.create(token=refresh_token)

        return JsonResponse({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)


class ActivationView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            
        #token, created = Token.objects.get_or_create(user=user)
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'detail': 'Account activated successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid activation link.'}, status=status.HTTP_400_BAD_REQUEST)

