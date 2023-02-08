from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'show_categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'categories__name', 'author__username')
    date_hierarchy = 'published'
    list_filter = ('categories__name',)

    def show_categories(self, object):
        return '-'.join([cat.name for cat in object.categories.all()])

    show_categories.short_description = 'Categorias'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
