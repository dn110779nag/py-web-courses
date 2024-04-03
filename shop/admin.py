from django.contrib import admin
from . import models

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcome to the Courses admin area"


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


admin.site.register(models.Course, CoursesAdmin)
admin.site.register(models.Category, CategoryAdmin)
