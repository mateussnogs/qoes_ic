from django.shortcuts import render

# Create your views here.

videos_paths = {}
videos_paths['first_session'] = ['Sublime - Santeria-AEYN5w4T_aM.mp4', 'Pink Floyd - Coming Back To Life-yjoPWxmOCtc.webm']

def video_sessions(request, session_num, video_num):
    if session_num == 1:
        if video_num == 1:
            video_path = videos_paths['first_session'][0]
        else:
            video_path = videos_paths['first_session'][1]
    elif session_num == 2:
        if video_num == 1:
            video_path = videos_paths['second_session'][0]
        else:
            video_path = videos_paths['third_session'][1]
    context = {
        'video_path':video_path
    }

    return render(request, 'video_sessions/video_session.html', context)
