from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='post_index'),
    url(r'^(?P<slug>[a-z0-9-]+)$', views.show, name='post_show'),
    url(r'^tags/(?P<slug>[a-z0-9-]+)$', views.index_by_tags, name='post_tag'),
]
