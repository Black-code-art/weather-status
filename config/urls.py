from django.contrib import admin
from django.urls import path,include
from django.http import JsonResponse
from django.urls import re_path
from rest_framework import permissions,authentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

def welcome(request):
    return JsonResponse(
        {
            "message": "Welcome to my API",
            "status": 200,
        }
    )
schema_view = get_schema_view(
   openapi.Info(
      title="Weather API",
      default_version='v1',
      description="API",
      terms_of_service="",
      contact=openapi.Contact(email="emmanuelebube117@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes= (authentication.BasicAuthentication,)
)



urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('admin/', admin.site.urls),
    path('accounts/',include("accounts.urls")),
    
]

