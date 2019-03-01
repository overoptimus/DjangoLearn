from django.db import models

# Create your models here.

class Grades(models.Model):
    # 自定义模型管理器
    # 当自定模型管理器，objects就不存在了
    # gradesObj = models.Manager()
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.gname
'''
    class Meta:
        db_table = ''
        ordering = []
'''


class StudentsManager(models.Manager):

    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(isDelete=False)

    def createStudent(self, name, gender, age, condent, grade, isD=False):
        stu = self.model()
        stu.sname = name
        stu.sgender = gender
        stu.sage = age
        stu.scondent = condent
        stu.sgrade = grade
        return stu


class Students(models.Model):
    stuObj = StudentsManager()
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scondent = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades",on_delete=models.DO_NOTHING)    #关联外键

    def __str__(self):
        return self.sname

    @classmethod
    def createStudent(cls, name, gender, age, condent, grade, isD=False):
        student = cls(sname=name, sgender=gender, sage=age, scondent=condent, isDelete=isD, sgrade=grade)
        return student
