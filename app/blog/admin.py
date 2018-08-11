from django.contrib import admin
# from django.db import models
# from pagedown.widgets import AdminPagedownWidget
from .models import Post, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    list_display_links = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    # formfield_overrides = {
    #     models.TextField: {'widget': AdminPagedownWidget}
    # }
