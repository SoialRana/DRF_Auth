from django.urls import path,include
from rest_framework import routers
from . views import ProductReviewViewSet,ProductViewSet

router=routers.DefaultRouter()
router.register('products', ProductViewSet,basename='products')
router.register('reviews', ProductReviewViewSet,basename='product-review')

# router.register('products', ProductViewSet)
# router.register('reviews', ProductReviewViewSet)

urlpatterns = [
    path('',include(router.urls)),
    # path('api_auth/',include("rest_framework.urls")),
    
]