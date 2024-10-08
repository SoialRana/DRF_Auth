from rest_framework import serializers
from .models import Product,ProductReview

class ProductSerializer(serializers.ModelSerializer):
    # reviews=serializers.StringRelatedField(many=True)
    class Meta:
        model=Product
        fields='__all__'
        
class ProductReviewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=ProductReview
        fields='__all__'