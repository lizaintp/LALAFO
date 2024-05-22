from django.contrib import admin
from apps.posts import models
# Register your models here.

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price']
