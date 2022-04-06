from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ['id','user','Title','Post','is_private']

admin.site.register(Post,PostAdmin)