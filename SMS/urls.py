from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view=get_schema_view(
    openapi.Info(
        title='Employee Management System',
        default_version='v1',
        description='To manage the full employee information'
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('employee.urls')),
    path('swagger/',schema_view.with_ui(cache_timeout=0),name='Swagger UI')
]
