from django.contrib import admin
from .models import Task, StatusTask, Course, StatusCourse


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'get_teachers', 'get_students', 'Start_date', 'Deadline', 'status']
    search_fields = ['name', 'course__name', 'Teacher__first_name', 'Student__first_name', 'Teacher__last_name',
                     'Student__last_name', 'status__name']

    def get_teachers(self, obj):
        return ",\n".join([str(teacher) for teacher in obj.Teacher.all()])

    def get_students(self, obj):
        return ",\n".join([str(student) for student in obj.Student.all()])

    get_teachers.short_description = 'Преподаватели'
    get_students.short_description = 'Студенты'


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_teachers', 'get_students', 'status']
    search_fields = ['name', 'teachers__first_name', 'students__first_name', 'teachers__last_name',
                     'students__last_name', 'status__name']

    def get_teachers(self, obj):
        return ",\n".join([str(teacher) for teacher in obj.teachers.all()])

    def get_students(self, obj):
        return ",\n".join([str(student) for student in obj.students.all()])

    get_teachers.short_description = 'Преподаватели'
    get_students.short_description = 'Студенты'


admin.site.register(StatusTask)
admin.site.register(Task, TaskAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(StatusCourse)
