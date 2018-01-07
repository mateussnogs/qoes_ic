
from django.urls import path, re_path

from . import views

app_name = 'video_sessions'

urlpatterns = [
    re_path(r'^video_sessions/(?P<video_session>[0-9]{2})/(?P<video_num>[0-9]{1})/$', views.video_sessions, name='video_sessions'),
]
