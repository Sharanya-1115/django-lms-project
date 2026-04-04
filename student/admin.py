from django.contrib import admin
from student.models import studentDetails
from student.models import member
# Register your models here.
admin.site.register(studentDetails)
admin.site.register(member)