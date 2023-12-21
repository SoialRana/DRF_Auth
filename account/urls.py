from django.urls import path
from .import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    # path('activate/<str:uidb64>/<str:token>/', views.ActivationView.as_view(), name='activate'),
    path('activate/<uidb64>/<token>/', views.ActivationView.as_view(), name='activate'),
]
