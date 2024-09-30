from django.urls import path
from .import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView,TokenObtainPairView
urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('activate/<str:token>/', views.ActivationView.as_view(), name='activate'),    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.LoginApi.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('change_password/', views.UserPasswordChangeView.as_view(), name='change_password'),
    path('password_reset/', views.PasswordResetEmailView.as_view(), name='password_reset_email'),
    path('reset-password/<str:token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),# path('reset/', views.SendPasswordResetEmailView.as_view(), name='reset'),
    
    
    # path('reset_password/<uid>/<token>/', views.UserPasswordResetView.as_view(), name='reset_password'),
    # path('token/blacklist/', views.BlackListTokenView.as_view(), name='token_blacklist'),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('activate/<str:uidb64>/<str:token>/', views.ActivationView.as_view(), name='activate'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('',views.home),
    # path('excp/',views.excp),
    # path('user/',views.user_info),
    # path('activate/<uidb64>/<token>/', views.ActivationView.as_view(), name='activate'),
]
