from django.urls import path,include
from rest_framework import routers
from . views import PostView

router=routers.DefaultRouter()
router.register('post', PostView,basename='post')


urlpatterns = [
    path('',include(router.urls)),
    path('api_auth/',include("rest_framework.urls")),
]