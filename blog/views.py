from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAdminUser,DjangoModelPermissionsOrAnonReadOnly,DjangoModelPermissions,IsAuthenticatedOrReadOnly,DjangoObjectPermissions
from . permissions import PostUserWritePermissions
# Create your views here.

class PostView(viewsets.ModelViewSet):
    permission_classes=[PostUserWritePermissions]
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
