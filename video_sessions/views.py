from django.shortcuts import render
from .forms import FeedbackForm, StressForm
from django.urls import reverse
from django import forms
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
import random
# Create your views here.

def video_sessions(request, session_num, video_num, session_announced):
    if 'already_watched' not in request.session:
        request.session['already_watched'] = []

    if session_num not in request.session['already_watched']:
        request.session['already_watched'].append(session_num)
        request.session.modified = True

    print("sessoes ja assistidas:")
    print(request.session['already_watched'])

    context = {
        'session_num_view': session_num,
        'video_num_view': video_num,
        'video_path': ''
    }
    if context['video_num_view'] == '3': #  = se a sessão ja mostrou os dois videos anteriores:
        #context['session_num_view'] = str(int(context['session_num_view']) + 1) # oldway em sequência e nao randomico
        context['session_num_view'] = str(context['session_num_view'])
        context['video_num_view'] = 1
        return HttpResponseRedirect(reverse('video_sessions:feedback', kwargs={'session_num':context['session_num_view']}))


    if session_announced == '0':
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
    return render(request, 'video_sessions/session_introd.html', context)

def feedback(request, session_num):
    session_announced = 0
    if request.method == "POST":
        if session_num == get_last_session(): #checar se o experimento terminou
            form = StressForm(request.POST)
            if form.is_valid():
                feed = form.save(commit=False)
                feed.estresse = form.cleaned_data.get('estresse')
                feed.num_sessao = str(session_num)
                if 'email' in request.session:
                    feed.email = str(request.session['email'])
                else:
                    feed.email = form.cleaned_data.get('email')
                feed.published_date = timezone.now()
                feed.save()
                next_session = get_next_random_session(request.session['already_watched'])
                return redirect('video_sessions:video_sessions', session_num = next_session, video_num = 1, session_announced = 1)
        else:
            form = FeedbackForm(request.POST)
            if form.is_valid():
                feed = form.save(commit=False)
                feed.num_sessao = str(session_num)
                feed.num_video_preferido = form.cleaned_data.get('num_video_preferido')
                feed.justificativa = form.cleaned_data.get('justificativa')
                feed.comment = form.cleaned_data.get('comment')

                if 'email' in request.session:
                    feed.email = str(request.session['email'])
                else:
                    feed.email = form.cleaned_data.get('email')
                    request.session['email'] = feed.email
                feed.published_date = timezone.now()
                feed.save()

                if len(request.session['already_watched']) >= 4: # se o usuário já assistiu 4 sessoes, termina experimento!
                    next_session = '9'
                    session_announced = 1

                else:
                    #selecionando nova sessao aleatoriamente
                    next_session = get_next_random_session(request.session['already_watched'])

                return redirect('video_sessions:video_sessions', session_num = next_session, video_num = 1, session_announced=session_announced)
    else:
        if session_num == get_last_session():
            if "email" in request.session:
                form = StressForm(initial={'email':request.session['email']})
            else:
                form = StressForm();
        else:
            if "email" in request.session:
                form = FeedbackForm(initial={'email':request.session['email']})
            else:
                form = FeedbackForm()

    context = {
        'form': form,
        'session_num': session_num,
    }
    return render(request, 'video_sessions/form_feedback.html', context)

def get_last_session():
    return str(8) #8 é a última sessão atualmente

def get_next_random_session(already_watched_array):
    next_session = str(random.randrange(1, 8)) # 1 até 7 incluso, pq o 8 é obrigatório
    while next_session in already_watched_array:
        next_session = str(random.randrange(1, 8))
    return next_session
