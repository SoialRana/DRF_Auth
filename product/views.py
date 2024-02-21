from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from . import models, serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import BasicAuthentication
from . permissions import AdminOrReadOnly
# from django_filters.rest_framework import DjangoFilterBackend
from accounts.models import BlacklistedToken
from rest_framework import filters
from . customauth import CustomAuthentication
from . permissions import MyPermission,AdminOrReadOnly,ReviewerOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductSerializer
    permission_classes=[IsAuthenticated]
    # permission_classes=[AdminOrReadOnly]
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [CustomAuthentication]
    authentication_classes = [JWTAuthentication]
    
    
class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset=models.ProductReview.objects.all()
    serializer_class=serializers.ProductReviewSerializer
    permission_classes = [ReviewerOrReadOnly]
    authentication_classes=[CustomAuthentication]

    # def create(self, request, *args, **kwargs):
    #     # Check if the access token is valid and not blacklisted
    #     access_token = request.auth

    #     if access_token and not BlacklistedToken.objects.filter(token=str(access_token)).exists():
    #         # Access token is valid
    #         response = super().create(request, *args, **kwargs)
    #         return response

    #     # Access token is either missing or blacklisted
    #     return Response({'detail': 'Authentication credentials were not provided or are invalid.'}, status=status.HTTP_401_UNAUTHORIZED)