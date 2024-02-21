from django.urls import path,include
from rest_framework import routers
from . views import ProductReviewViewSet,ProductViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router=routers.DefaultRouter()
router.register('products', ProductViewSet,basename='products')
router.register('reviews', ProductReviewViewSet,basename='product-review')

# router.register('products', ProductViewSet)
# router.register('reviews', ProductReviewViewSet)

urlpatterns = [
    path('',include(router.urls)),
    # path('api_auth/',include("rest_framework.urls")),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
]