from django.urls import path
from .views import EmployeeDetailsViews

urlpatterns=[

        path('employees/',EmployeeDetailsViews.as_view()),
        path('employees/<int:id>',EmployeeDetailsViews.as_view()),
        

    
    ]
