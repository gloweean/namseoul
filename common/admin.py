from django.contrib import admin
from .models import Bible

# Register your models here.

@admin.register(Bible)
class BibleAdmin(admin.ModelAdmin):
    pass