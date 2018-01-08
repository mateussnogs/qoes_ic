from django.shortcuts import render
from .forms import FeedbackForm
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
# Create your views here.

def video_sessions(request, session_num, video_num):
    context = {
        'session_num_view': session_num,
        'video_num_view': video_num,
        'video_path': ''
    }

    if context['video_num_view'] == '2':
        context['session_num_view'] = str(int(context['session_num_view']) + 1)
        context['video_num_view'] = 0
        return HttpResponseRedirect(reverse('video_sessions:feedback', kwargs={'session_num':context['session_num_view']}))

    #decidindo qual path de video retornar
    if session_num == '1':
        if video_num == '1':
            context['video_path'] = "The Smashing Pumpkins - Tonight, Tonight-NOG3eus4ZSo.mp4"
        elif video_num == '2':
            context['video_path'] = "Sublime - Santeria-AEYN5w4T_aM.mp4"

    return render(request, 'video_sessions/video_session.html', context)

def feedback(request, session_num):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.author = form.cleaned_data.get('author')
            feed.num_sessao = session_num
            feed.num_video_preferido = form.cleaned_data.get('num_video_preferido')
            feed.text = form.cleaned_data.get('text')
            feed.published_date = timezone.now()
            feed.save()
            return redirect('video_sessions:video_sessions', session_num = session_num, video_num = 1 )
    else:
        form = FeedbackForm()
    return render(request, 'video_sessions/form_feedback.html', {'form': form, 'session_num': session_num})
