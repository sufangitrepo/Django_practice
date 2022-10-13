from django.contrib import admin
from firstapp.models import StudentModel

# Register your models here.

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'father_name', 'roll_no']