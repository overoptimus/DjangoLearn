from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Students,Grades
from django.db.models import Max,F,Q
import sys

def index(request):
    g = Grades.objects.filter(gboynum__gt=F('ggirlnum'))
    print(g)
    return render(request, 'myApp/index.html')

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

def verifyCode(request):
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), random.randrange(20, 100))
    width = 100
    height = 50
    # 创建画面对象
    im = Image.new('RGB', (width, height), color=bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point（）函数绘制噪点
    for i in range(80):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str[random.randrange(0, len(str))]
    # 构造字体对象
    font = ImageFont.truetype(font='/static/myApp/font/verdanab.ttf', size=40)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    draw.text((5, 2), rand_str[0], fill=fontcolor, font=font)
    draw.text((25, 2), rand_str[1], fill=fontcolor, font=font)
    draw.text((50, 2), rand_str[2], fill=fontcolor, font=font)
    draw.text((75, 2), rand_str[3], fill=fontcolor, font=font)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

def checkverifycode(request):
    userInput = request.POST.get('verifycode').upper()
    verifyCode = request.session['verifycode'].upper()
    if userInput == verifyCode:
        return HttpResponse(content='成功')
    else:
        request.session['flag'] = False
        return redirect('/sunck/verifycodefile')

def verifycodefile(request):
    f = request.session.get('flag', True)
    print(f)
    str1 = ''
    if f == False:
        str1 = '请重新输入'
    request.session.clear()
    return render(request, 'myApp/verifycodefile.html', {'flag': str1})

def upfile(request):
    return render(request, 'myApp/upfile.html')


import os
from django.conf import settings

def savefile(request):
    if request.method == 'POST':
        f = request.FILES['file']
        # 合成文件在服务器端的路径
        filepath = os.path.join(settings.MEDIA_ROOT, f.name)
        with open(filepath, 'wb') as fp:
            for info in f.chunks():
                fp.write(info)
        return HttpResponse(content='上传成功')
    else:
        return HttpResponse(content='上传失败')

from django.core.paginator import Paginator
def studentspage(request, pageId):
    allList = Students.stuObj.all()
    paginator = Paginator(allList, 2)
    page = paginator.page(pageId)
    return render(request, 'myApp/studentspage.html', {'students': page})

def ajaxstudents(request):
    return render(request, 'myApp/ajaxstudents.html')


from django.http import JsonResponse
def studentsinfo(request):
    stus = Students.stuObj.all()
    print(type(stus))
    list = []
    for stu in stus:
        list.append([stu.sname, stu.sage])
    return JsonResponse({"students": list})


def edit(request):
    return render(request, 'myApp/edit.html')

import time
from .task import task1
def celerytest(request):
    task1.delay()
    return render(request, 'myApp/celeryTest.html')
