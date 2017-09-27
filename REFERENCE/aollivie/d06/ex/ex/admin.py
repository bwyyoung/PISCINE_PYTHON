from django.contrib import admin
from .models import MyUser
# Register your models here.

class MyUserAdmin(admin.ModelAdmin):
    model = MyUser
    fields = ['username', 'groups']

admin.site.register(MyUser, MyUserAdmin)
