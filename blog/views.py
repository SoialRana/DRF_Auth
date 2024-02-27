from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAdminUser,DjangoModelPermissionsOrAnonReadOnly,DjangoModelPermissions,IsAuthenticatedOrReadOnly,DjangoObjectPermissions
from . permissions import PostUserWritePermissions
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .customauth import CustomAuthentication
# Create your views here.

class PostView(viewsets.ModelViewSet):
    authentication_classes=[JWTAuthentication]
    # authentication_classes=[BasicAuthentication]
    # authentication_classes=[CustomAuthentication]
    permission_classes=[PostUserWritePermissions]
    # permission_classes=[AllowAny]
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
