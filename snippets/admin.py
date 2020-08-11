from django.contrib import admin
from . import models


USER_SEARCH_FILTER = ('user__username', 'user__email', 'user__first_name', 'user__last_name')


@admin.register(models.Group)
class Group(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'creation_date')
    search_fields = ('name',)
    list_filter = ('type',)
    readonly_fields = ('creation_date', 'id')
    date_hierarchy = 'creation_date'
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 15
    fieldsets = (
        ('Information', {'fields': ('id', 'logo', ('name', 'slug'), 'description')}),
        ('Status', {'fields': ('type', 'creation_date')})
    )


@admin.register(models.Member)
class Member(admin.ModelAdmin):
    list_display = ('id', 'group', 'user', 'status', 'date_joined')
    search_fields = ('group__name', *USER_SEARCH_FILTER)
    list_filter = ('group__type', 'user__is_staff', 'status')
    readonly_fields = ('date_joined', 'id')
    date_hierarchy = 'date_joined'
    list_per_page = 15
    fieldsets = (
        ('Information', {'fields': ('id', 'group', 'user')}),
        ('Status', {'fields': ('date_joined', 'status')})
    )


@admin.register(models.InviteLink)
class InviteLink(admin.ModelAdmin):
    list_display = ('invite_id', 'group', 'status', 'users_joined', 'creation_date')
    search_fields = ('group__name', 'invite_id')
    date_hierarchy = 'creation_date'
    list_filter = ('status', 'group__type', 'status')
    readonly_fields = ('invite_id', 'creation_date')
    list_per_page = 15
    fieldsets = (
        ('Information', {'fields': ('invite_id', 'group', 'users_joined')}),
        ('Status', {'fields': ('status', 'creation_date')})
    )


@admin.register(models.UserInvite)
class UserInvite(admin.ModelAdmin):
    list_display = ('id', 'user', 'group', 'status', 'creation_date')
    search_fields = ('group__name', *USER_SEARCH_FILTER)
    list_filter = ('status', 'group__type', 'user__is_staff')
    readonly_fields = ('creation_date', 'id')
    date_hierarchy = 'creation_date'
    list_per_page = 15
    fieldsets = (
        ('Information', {'fields': (('user', 'group'),)}),
        ('Status', {'fields': ('status', 'creation_date')})
    )


@admin.register(models.Snippet)
class Snippet(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'group', 'status', 'lang', 'creation_date')
    search_fields = ('name', 'group__name', *USER_SEARCH_FILTER)
    list_filter = ('status', 'group__type', 'user__is_staff', 'lang')
    readonly_fields = ('creation_date', 'id')
    date_hierarchy = 'creation_date'
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 15
    fieldsets = (
        ('Information', {'fields': (('name', 'slug'), ('code', 'lang'), ('group', 'user'))}),
        ('Status', {'fields': ('status', 'creation_date')}),
        ('Description', {'fields': ('description',)})
    )
    
    
@admin.register(models.TelegramGroup)
class TelegramGroup(admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'group')
    search_fields = ('name', 'chat_id', 'id', 'link', 'group__name')
    list_filter = ('group__type',)
    readonly_fields = ('id',)
    date_hierarchy = 'group__creation_date'
    list_per_page = 15
    fieldsets = (
        ('Information', {'fields': ('id', 'chat_id', 'group')}),
    )


@admin.register(models.ScreenShot)
class ScreenShot(admin.ModelAdmin):
    list_display = ('id', 'snippet')
    search_fields = ('id', 'snippet__name', 'snippet__user__username')
    readonly_fields = ('id',)
    list_per_page = 15
    fieldsets = (('Information', {'fields': ('id', 'snippet')}),)
