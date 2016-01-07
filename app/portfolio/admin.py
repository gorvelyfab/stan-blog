from django.contrib import admin

from .models import Work, Category, WorkPicture


class WorkPictureInline(admin.StackedInline):
    model = WorkPicture


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [WorkPictureInline]
