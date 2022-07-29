from django.contrib import admin
from .models import Student
from .models import User

# Register your models here.
# admin.site.register(Student)
admin.site.register(User)

@admin.register(Student)
class Student_DetailAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','pass1']
    list_filter = ['fname']
    search_fields = ('fname__startswith',)
    

