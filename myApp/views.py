from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Students,Grades
from django.db.models import Max,F,Q
import sys

def index(request):
    g = Grades.objects.filter(gboynum__gt=F('ggirlnum'))
    print(g)
    return HttpResponse('sunck is a good man!')

def index1(request):
    return HttpResponseRedirect('/sunck')

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

def students1(request):
    studentsList = Students.stuObj.all()[0:2]
    return render(request, 'myApp/students.html', {'students': studentsList})


def students2(request, page):
    studentsList = Students.stuObj.all()[(page-1)*2:page*2]
    return render(request, 'myApp/students.html', {'students': studentsList})


def studentsearch(request):
    maxAge = Students.stuObj.aggregate(Max('sage'))
    print(maxAge)
    studentsList = Students.stuObj.filter(Q(pk__lte=2) | Q(sage__gt=50))
    print(studentsList)
    # 学生描述中带有薛艳梅的学生所在班级的集合
    gradesList = Grades.objects.filter(students__scondent__contains='薛艳梅')
    print(gradesList)
    return HttpResponse('1111')

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

def attribles(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse('123123123123123')

def get1(request):
    a = request.GET.get('a')
    b = request.GET['b']
    c = request.GET.get('c')
    return HttpResponse(a +  "     "  + b + "   " + c)

def get2(request):
    aList = request.GET.getlist('a')
    a1 = aList[0]
    a2 = aList[1]
    b = request.GET.get('c')
    return HttpResponse(str(a1) + "   " + str(a2) + "   " + str(b))

def showregist(request):
    return render(request, 'myApp/regist.html')

def regist(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    hobbyList = request.POST.getlist('hobby')
    print(name)
    print(gender)
    print(age)
    print(hobbyList)
    return HttpResponse('post')

def showresponse(request):
    res = HttpResponse(content=b'dawdafawdadadw')
    print(res.content)
    print(res.charset)
    print(res.status_code)
    return res

def cookietest(request):
    res = HttpResponse()
    # res.set_cookie('sunck', value='good', max_age=None, expires=None, path='/', domain=None, secure=False, httponly=False, samesite=None)
    cookies = request.COOKIES
    res.write('<h1>' + cookies['sunck'] + '</h1>')
    return res

def redirect1(request):
    # return HttpResponseRedirect('/sunck/redirect2/')
    return redirect('/sunck/redirect2')
def redirect2(request):
    return HttpResponse(content='我是重定向之后的页面')


#session
def main(request):
    username = request.session.get('name', '游客')
    return render(request, 'myApp/main.html', {'username': username})

def login(request):
    return render(request, 'myApp/login.html')

def showmain(request):
    username = request.POST.get('username')
    request.session['name'] = username
    return redirect('/sunck/main/')

from django.contrib.auth import logout
def quit(request):
    # 清除session
    # 推荐使用logout()
    logout(request)
    # request.session.clear()
    # request.session.flush()
    return redirect('/sunck/main/')


def good(request):
    return HttpResponse(content='good')

def zhuye(request):
    return render(request, 'myApp/index.html')

def detail(request):
    return render(request, 'myApp/detail.html')

def postfile(request):
    return render(request, 'myApp/postfile.html')

def showname(request):
    user = request.POST.get('username')
    pwd = request.POST.get('passwd')
    return render(request, 'myApp/showname.html', {'username': user, 'passwd': pwd})
