from django.contrib import admin

# Register your models here.
from myApp.models import Grades,Students


class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2


@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    #列表页属性
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    #添加修改页属性
    #fields = []
    fieldsets =[
        ('num', {'fields': ['ggirlnum', 'gboynum']}),
        ('base', {'fields': ['gname', 'gdate', 'isDelete']}),
    ]
    inlines = [StudentsInfo]





#admin.site.register(Grades, GradesAdmin)


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    gender.short_description = '性别'

    def name(self):
        return self.sname
    name.short_description = '姓名'

    def age(self):
        return self.sage
    age.short_description = '年龄'

    def condent(self):
        return self.scondent
    condent.short_description = '简介'

    def grade(self):
        return self.sgrade
    grade.short_description = '班级'


    #列表页属性
    list_display = ['pk', name, age, condent, gender, grade, 'isDelete']
    list_filter = ['sgrade']
    search_fields = ['sname']
    list_per_page = 2

    #添加修改页属性
    #fields = []
    #fieldsets =[
    #    ('num', {'fields': ['ggirlnum', 'gboynum']}),
    #    ('base', {'fields': ['gname', 'gdate', 'isDelete']}),
    #s]
    #actions_on_bottom = True




#admin.site.register(Students, StudentsAdmin)
