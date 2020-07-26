from django.contrib import admin

from utils.functions import check_self_article_or_supper_user
from . import models
from django.http import HttpRequest


@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = ('name', 'slug', 'sub_category')
    search_fields = ('name', 'slug', 'sub_category__name')
    list_per_page = 15
    fieldsets = (('Information', {'fields': ('name', 'slug', 'sub_category')}),)


@admin.register(models.Article)
class Article(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'status', 'get_categories')
    search_fields = ('author__username', 'author__email', 'title', 'category__name')
    list_filter = ('status', 'author__is_staff')
    date_hierarchy = 'date'
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 15
    readonly_fields = ('date',)
    fieldsets = (
        ('Information', {'fields': (('title', 'slug'), 'categories')}),
        ('Status', {'fields': ('status', 'date')}),
        ('Content', {'fields': ('content',)})
    )

    def get_categories(self, categories):
        return ', '.join([category.name for category in categories.objects.all()[:5]])

    def has_delete_permission(self, request: HttpRequest, obj: models.Article = None):
        return super().has_delete_permission(request, obj) and check_self_article_or_supper_user(request, obj)

    def has_change_permission(self, request: HttpRequest, obj: models.Article = None):
        return super().has_change_permission(request, obj) and check_self_article_or_supper_user(request, obj)


@admin.register(models.Comment)
class Comment(admin.ModelAdmin):
    list_display = ('date', 'author', 'article', 'status')
    search_fields = ('author__username', 'author__email', 'article__title', 'content')
    list_filter = ('status', 'author__is_staff')
    date_hierarchy = 'date'
    list_per_page = 15
    readonly_fields = ('date',)
    fieldsets = (
        ('Information', {'fields': (('article',),)}),
        ('Status', {'fields': ('status', 'date')}),
        ('Content', {'fields': ('content',)})
    )