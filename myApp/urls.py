from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:num>/',views.detail),
    path('grades/',views.grades),
    path('students/', views.students),
    path('grades/<int:id>/', views.gradeStudents),
    path('addstudent/', views.addStudent),
]
