from django.urls import path, re_path

from . import views

app_name = 'core'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^categories/$', views.categories, name='categories'),
    re_path(r'^en/$', views.en_index, name='en_index'),
    re_path(r'^(?P<english>\w*)/?categories/$', views.categories, name='en_categories'),
]
