from django.contrib import admin

from students.models import Student

# admin.site.register(Student) this is for simple showing the data inn admin panel


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display= ('name' , 'age')
    search_fields=('name','age')
    list_filter=('age','city')
    ordering=('name',)



# def __str__(Student)
#     return self.name (when you write the code for the customizaation like abovethen)
# you dont need to write the fucntion inside the models.py 