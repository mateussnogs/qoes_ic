from django.shortcuts import render
from .forms import FeedbackForm, StressForm
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
# Create your views here.

def video_sessions(request, session_num, video_num, session_announced):
    context = {
        'session_num_view': session_num,
        'video_num_view': video_num,
        'video_path': ''
    }
    if context['video_num_view'] == '3':
        context['session_num_view'] = str(int(context['session_num_view']) + 1)
        context['video_num_view'] = 1
        return HttpResponseRedirect(reverse('video_sessions:feedback', kwargs={'session_num':context['session_num_view']}))

    if session_announced == '0':
        print("wtfraifadiofasio")
        return HttpResponseRedirect(reverse('video_sessions:session_introd', kwargs={'session_num':context['session_num_view']}))

    #decidindo qual path de video retornar
    if session_num == '1':
        if video_num == '1':
            context['video_path'] = "brasil_perde_alemanha_sliced.mp4"
        elif video_num == '2':
            context['video_path'] = "brasil_ganha_alemanha_sliced_rebuffs.mp4"
    elif session_num == '2':
        if video_num == '1':
            context['video_path'] = "porta_dos_fnds_rebuffs.mp4"
        elif video_num == '2':
            context['video_path'] = "parafernalha_sliced.mp4"
    elif session_num == '3':
        if video_num == '1':
            context['video_path'] = "skol.mp4"
        elif video_num == '2':
            context['video_path'] = "Piratas do Caribe_sliced_rebuffs.mp4"
    elif session_num == '4':
        if video_num == '1':
            context['video_path'] = "pandas_sliced_rebuffs.mp4"
        elif video_num == '2':
            context['video_path'] = "zen_music_diving_sea_sliced.mp4"

    elif session_num == '5':
        if video_num == '1':
            context['video_path'] = "radicais_composto_rebuffs.mp4"
        elif video_num == '2':
            context['video_path'] = "slack_sliced.mp4"

    elif session_num == '6':
        if video_num == '1':
            context['video_path'] = "formigas.mp4"
        elif video_num == '2':
            context['video_path'] = "onca_composto_rebuffs.mp4"

    elif session_num == '7':
        if video_num == '1':
            context['video_path'] = "buracos_negros_rebuffs.mp4"
        elif video_num == '2':
            context['video_path'] = "newton.mp4"

    elif session_num == '8':
        if video_num == '1':
            context['video_path'] = "usain_disturbed.mp4"
        elif video_num == '2':
            context['video_path'] = "usain_sliced_hd.mp4"
    else:
        return render(request, 'video_sessions/final.html')
    return render(request, 'video_sessions/video_session.html', context)

def session_introd(request, session_num):
    context = {
        'session_num_view':session_num,
    }
    print(context['session_num_view'])
    return render(request, 'video_sessions/session_introd.html', context)

def feedback(request, session_num):
    if request.method == "POST":
        if session_num == get_last_session():
            form = StressForm(request.POST)
            if form.is_valid():
                feed = form.save(commit=False)
                feed.estresse = form.cleaned_data.get('estresse')
                feed.num_sessao = str(int(session_num) - 1)
                feed.justificativa = form.cleaned_data.get('justificativa')
                feed.rebuff_feedback = form.cleaned_data.get('rebuff_feedback')
                feed.recommend_feedback = form.cleaned_data.get('recommend_feedback')
                feed.email = form.cleaned_data.get('email')
                feed.published_date = timezone.now()
                feed.save()
                return redirect('video_sessions:video_sessions', session_num = session_num, video_num = 1, session_announced=1)
        else:
            form = FeedbackForm(request.POST)
            if form.is_valid():
                feed = form.save(commit=False)
                feed.num_sessao = str(int(session_num) - 1)
                feed.num_video_preferido = form.cleaned_data.get('num_video_preferido')
                feed.justificativa = form.cleaned_data.get('justificativa')
                feed.comment = form.cleaned_data.get('comment')
                feed.email = form.cleaned_data.get('email')
                feed.published_date = timezone.now()
                feed.save()
                return redirect('video_sessions:video_sessions', session_num = session_num, video_num = 1, session_announced=0)
    else:
        if session_num == get_last_session():
            form = StressForm();
        else:
            form = FeedbackForm()

    context = {
        'form': form,
        'session_num': session_num,
    }
    return render(request, 'video_sessions/form_feedback.html', context)

def get_last_session():
    return str(8+1) #8 é a última sessão atualmente, e +1 pra cancelar uma gambiarra e chegar a 9
