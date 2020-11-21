from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(diamonds, earring, rings)
class ViewAdmin(admin.ModelAdmin):
    pass
