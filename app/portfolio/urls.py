from django.urls import path

from . import views

app_name = 'work'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.show, name='show'),
]
