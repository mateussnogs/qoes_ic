
from django.urls import path, re_path

from . import views

app_name = 'video_sessions'

urlpatterns = [
    re_path(r'^session(?P<session_num>\d)/video(?P<video_num>\d)/(?P<session_announced>[0-1])/$', views.video_sessions, name='video_sessions'),
    re_path(r'^feedback/session(?P<session_num>\d)/$', views.feedback, name='feedback'),
    re_path(r'^introducao/session(?P<session_num>\d)/$', views.session_introd, name="session_introd"),
]
