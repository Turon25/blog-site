from django.contrib import admin
from django.template.defaultfilters import title

from .models import Post
# Register your models here.
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status', 'created','publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = ('publish',)
    ordering = ('status', 'publish')
