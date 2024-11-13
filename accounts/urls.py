from django.urls import path,  include
from .views import*

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('user', UserViewSet, basename='users')


urlpatterns = [
    path('',include(router.urls)),
    path('login/',user_login),
    path('weather/', WeatherUpdateView.as_view())
    
]
