from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Students,Grades


def index(request):
    return HttpResponse('sunck is a good man!')


def detail(request, num, num2):
    return HttpResponse('detail-%s-%s' %(num,num2))

def grades(request):
    #去模型里取数据
    gradesList = Grades.objects.all()
    #将数据传递给模板，模板再进行渲染页面，将渲染好的页面返回浏览器
    return render(request, 'myApp/grades.html', {'grades': gradesList})


def students(request):
    studentsList = Students.stuObj.all()
    return render(request, 'myApp/students.html', {'students': studentsList})


def gradeStudents(request, id):
    grade = Grades.objects.get(pk=id)
    studentsList = grade.students_set.all()
    return render(request, 'myApp/gradeStudents.html', {'students': studentsList,   \
    'grade': grade})


def addStudent(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent("刘德华", True, 30, "我是刘德华", grade)
    stu.save()
    return HttpResponse('111')