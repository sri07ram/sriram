from django.urls import path
from .views import EmployeeCreateView,EmployeeGetView,EmployeeUpdateView,EmployeeDeleteView

urlpatterns=[
    path('employee/',EmployeeCreateView.as_view(),name='create'),
    path('employee/all',EmployeeGetView.as_view(),name='get'),
    path('employee/<int:pk>/update',EmployeeUpdateView.as_view(),name='update'),
    path('employee/<str:pk>/delete',EmployeeDeleteView.as_view(),name='delete')
]