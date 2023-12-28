from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes=[IsAuthenticated]
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductSerializer
    
class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset=models.ProductReview.objects.all()
    serializer_class=serializers.ProductReviewSerializer