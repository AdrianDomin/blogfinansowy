from django.contrib import admin
from .models import Post


# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'publish')
    list_filter = ('author', 'status', 'publish')
    search_filds = ( 'author', 'title', 'body')
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Post, PostAdmin)
