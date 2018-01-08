
from django.urls import path, re_path

from . import views

app_name = 'video_sessions'

urlpatterns = [
    re_path(r'^session(?P<session_num>\d)/video(?P<video_num>\d)/$', views.video_sessions, name='video_sessions'),
    re_path(r'^feedback/session(?P<session_num>\d)/$', views.feedback, name='feedback'),
]
