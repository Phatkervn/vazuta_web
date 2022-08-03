
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(App)
class app(admin.ModelAdmin):
    pass