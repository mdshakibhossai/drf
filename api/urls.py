from django.urls import path
from .views import *

urlpatterns = [
    path('hello/',hello),
    path('students/',student_list),
    path('student/<int:id>/', student_detail),
    
]
