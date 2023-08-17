from django.contrib import admin

from .models import *


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'user', 'description', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_filter = ('time_create',)
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'user', 'description', 'content', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update')


admin.site.register(Articles, ArticlesAdmin)

admin.site.site_title = 'Админ-панель статей'