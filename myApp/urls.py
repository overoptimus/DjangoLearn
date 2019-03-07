from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index),
    path('index', views.index1),
    path('<int:num>/', views.detail),
    path('grades/', views.grades),
    path('students/', views.students),
    path('students1/', views.students1),
    path('stu/<int:page>/', views.students2),
    path('studentsearch', views.studentsearch),
    path('grades/<int:id>/', views.gradeStudents),
    path('addstudent/', views.addStudent),
    path('attribles/', views.attribles),
    path('get1/', views.get1),
    path('get2/', views.get2),
    path('showregist/', views.showregist),
    path('regist/', views.regist),
    path('showresponse/', views.showresponse),
    path('cookietest', views.cookietest),
    path('redirect1/', views.redirect1),
    path('redirect2/', views.redirect2),
    path('main/', views.main),
    path('login/', views.login),
    path('showmain/', views.showmain),
    path('quit/', views.quit),
    path('good/', views.good, name = 'good'),
    path('zhuye/', views.zhuye),
    path('detail/', views.detail),
    path('postfile/', views.postfile),
    path('showname/', views.showname, name='showname'),
    path('verifycode/', views.verifyCode, name='verifycode'),
    path('checkverifycode', views.checkverifycode, name='checkverifycode'),
    path('verifycodefile/', views.verifycodefile)
]
