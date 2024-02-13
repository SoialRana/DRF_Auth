from django.urls import path
from .import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView,TokenObtainPairView
urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    # path('login/', views.LoginApi.as_view(), name='login'),
    # path('activate/<str:uidb64>/<str:token>/', views.ActivationView.as_view(), name='activate'),
    path('activate/<uidb64>/<token>/', views.ActivationView.as_view(), name='activate'),
    
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('',views.home),
    path('excp/',views.excp),
    path('user/',views.user_info),
]
