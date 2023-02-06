from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "date_updated"]
    prepopulated_fields = {'slug': ('title',)}
