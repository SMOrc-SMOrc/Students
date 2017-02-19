from django.contrib import admin
from .models import Students, RecordBook

class StudentList(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name')


class RecordBookList(admin.ModelAdmin):
    list_display = ('number', 'student')

admin.site.register(Students, StudentList)
admin.site.register(RecordBook, RecordBookList)


# Register your models here.
