from django.shortcuts import render
from .forms import FeedbackForm, StressForm, FeedbackForm_en, StressForm_en
from django.urls import reverse
from django import forms
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
import random
# Create your views here.

def video_sessions(request, session_num, video_num, session_announced, english=''):
    en = False
    if english == 'en':
        en = True
    if 'already_watched' not in request.session:
        request.session['already_watched'] = []

    if session_num not in request.session['already_watched']:
        request.session['already_watched'].append(session_num)
        request.session.modified = True

    context = {
        'session_num_view': session_num,
        'video_num_view': video_num,
        'video_path': '',
        'en_view_bool': en,
        'english_str': english,
    }

    if context['video_num_view'] == '3': #  = se a sessão ja mostrou os dois videos anteriores:
        #context['session_num_view'] = str(int(context['session_num_view']) + 1) # oldway em sequência e nao randomico
        context['session_num_view'] = str(context['session_num_view'])
        context['video_num_view'] = 1
        return HttpResponseRedirect(reverse('video_sessions:feedback', kwargs={'session_num':context['session_num_view'], 'english':english}))

    if session_announced == '0': # redirecionar para a pagina de introdução da sessão antes de exibi-la

        return HttpResponseRedirect(reverse('video_sessions:session_introd', kwargs={'session_num':context['session_num_view'], 'english':english}))

    if en:
        video_path = get_video_path_en(session_num, video_num)
    else:
        video_path = get_video_path(session_num, video_num)

    if video_path == None:
        return render(request, 'video_sessions/final.html', context)

    context['video_path'] = video_path
    return render(request, 'video_sessions/video_session.html', context)

def session_introd(request, session_num, english=''):
    context = {
        'session_num_view':session_num,
        'en_view_bool': False,
        'english_str': english

    }
    if english == 'en':
        context['en_view_bool'] = True
    return render(request, 'video_sessions/session_introd.html', context)

def feedback(request, session_num, english=''):
    en = False
    if english == 'en':
        en = True

    session_announced = 0
    if request.method == "POST":
        if session_num == get_last_session(): #checar se o experimento terminou
            if en:
                form = StressForm_en(request.POST)
            else:
                form = StressForm(request.POST)
            if form.is_valid():
                feed = form.save(commit=False)
                feed.estresse = form.cleaned_data.get('estresse')
                feed.num_sessao = str(session_num)
                if 'email' in request.session:
                    feed.email = str(request.session['email'])
                else:
                    feed.email = form.cleaned_data.get('email')
                    request.session['email'] = feed.email
                feed.published_date = timezone.now()
                if en:
                    feed.english = True
                feed.session_id = request.session.session_key
                feed.save()
                if en == False:
                    next_session = get_next_random_session(request.session['already_watched'])
                else:
                    next_session = get_next_session_en(session_num)
                return redirect('video_sessions:video_sessions', session_num = next_session, video_num = 1, session_announced = 0, english=english)
        else: # as sessoes dps das iniciais
            if en:
                form = FeedbackForm_en(request.POST)
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
                if en:
                    feed.english = True
                feed.session_id = request.session.session_key
                feed.save()

                if len(request.session['already_watched']) >= 4: # se o usuário já assistiu 4 sessoes, termina experimento!
                    next_session = str(999)
                    session_announced = 1

                else:
                    #selecionando nova sessao aleatoriamente
                    if en == False:
                        next_session = get_next_random_session(request.session['already_watched'])
                    else:
                        next_session = get_next_session_en(session_num)
                return redirect('video_sessions:video_sessions', session_num = next_session, video_num = 1, session_announced=session_announced, english=english)
    else:
        if session_num == get_last_session():
            if "email" in request.session:
                if en:
                    form = StressForm_en(initial={'email':request.session['email']})
                else:
                    form = StressForm(initial={'email':request.session['email']})
            else:
                if en:
                    form = StressForm_en()
                else:
                    form = StressForm()
        else:
            if "email" in request.session:
                if en:
                    form = FeedbackForm_en(initial={'email':request.session['email']})
                else:
                    form = FeedbackForm(initial={'email':request.session['email']})
            else:
                if en:
                    form = FeedbackForm_en()
                else:
                    form = FeedbackForm()

    context = {
        'form': form,
        'session_num': session_num,
        'english' : english,
    }
    return render(request, 'video_sessions/form_feedback.html', context)

def get_last_session():
    return str(8) #8 é a última sessão atualmente

def get_next_random_session(already_watched_array):
    next_session = str(random.randrange(1, 8)) # 1 até 7 incluso, pq o 8 é obrigatório
    while next_session in already_watched_array:
        next_session = str(random.randrange(1, 8))
    return next_session

def get_next_session_en(session_num):
    if session_num == str(8):
        return str(1)
    elif session_num == str(1):
        return str(7)
    elif session_num == str(7):
        return str(4)
    else:
        return str(666) # termina

def get_video_path_en(session_num, video_num):
    video_path = None
    if session_num == '1':
        if video_num == '1':
            video_path = "funny_cats_ytb.mp4"
        elif video_num == '2':
            video_path = "smart_dogs.mp4"
    else:
        video_path = get_video_path(session_num, video_num)
    return video_path

#decidindo qual path de video retornar, #retorna None se não houver mais videos
def get_video_path(session_num, video_num):
    video_path = None
    if session_num == '1':
        if video_num == '1':
            video_path = "brasil_perde_alemanha_sliced.mp4"
        elif video_num == '2':
            video_path = "brasil_ganha_ytb.mp4"
    elif session_num == '2':
        if video_num == '1':
            video_path = "sotaques.mp4"
        elif video_num == '2':
            video_path = "poser.mp4"
    elif session_num == '3':
        if video_num == '1':
            video_path = "pandas_ytb.mp4"
        elif video_num == '2':
            video_path = "zen_music_diving_sea_sliced.mp4"

    elif session_num == '4':
        if video_num == '1':
            video_path = "radicais_composto_rebuffs.mp4"
        elif video_num == '2':
            video_path = "slack_sliced.mp4"

    elif session_num == '5':
        if video_num == '1':
            video_path = "formigas.mp4"
        elif video_num == '2':
            video_path = "onca_ytb.mp4"

    elif session_num == '6':
        if video_num == '1':
            video_path = "buracos_negros_ytb.mp4"
        elif video_num == '2':
            video_path = "sistema_solar_telecurso_sliced.mp4"

    elif session_num == '7':
        if video_num == '1':
            video_path = "vivaldi_bad_qos.mp4"
        elif video_num == '2':
            video_path = "Vivaldi_g_qos.mp4"

    elif session_num == '8':
        if video_num == '1':
            video_path = "usain_disturbed.mp4"
        elif video_num == '2':
            video_path = "usain_sliced_hd.mp4"

    return video_path



def youtube_test(request):
    return render(request, 'video_sessions/youtube_test.html')
