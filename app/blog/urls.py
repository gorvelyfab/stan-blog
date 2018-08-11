from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='post_index'),
    path('<slug:slug>', views.show, name='post_show'),
    path('tags/<slug:slug>', views.index_by_tags, name='post_tag'),
]
