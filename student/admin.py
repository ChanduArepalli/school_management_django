from django.contrib import admin
from .models import Student
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'admin_no', 'section_name', 'class_name']
    search_fields = ['name', 'section_name']
    list_filter = ['attendance', 'section_name']


admin.site.register(Student, StudentAdmin)



