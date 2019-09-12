from django.contrib import admin
from .models import DjUser, Book
# Register your models here.


class DjUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(DjUser, DjUserAdmin)
admin.site.register(Book)