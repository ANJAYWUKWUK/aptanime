# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from aptanimelistweb.models import List



class AdminList(admin.ModelAdmin):
    list_display = ('judul','add_time')
admin.site.register(List,AdminList)