from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from video_sessions.forms import CategoriesForm, CategoriesForm_en
import random
from django.shortcuts import redirect
# Create your views here.


def index(request):
    request.session.clear()
    context = {
        'session_num_view' : str(8) # até 8 excluso, pq a oitava sessão é a última, e todos assistem
    }
    return render(request, 'index.html', context)

def en_index(request):
    request.session.clear()
    return render(request, 'en_index.html')

def categories(request, english=''):
    en = False
    if english == 'en':
        en = True
    if request.method == "POST":
        if en:
            form = CategoriesForm_en(request.POST)
        else:
            form = CategoriesForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.comedia = form.cleaned_data.get('comedia')
            feed.esporte = form.cleaned_data.get('esporte')
            feed.documentario = form.cleaned_data.get('documentario')
            feed.musica = form.cleaned_data.get('musica')
            if en:
                feed.english = True
            feed.session_id = request.session.session_key
            feed.save()
            return redirect('video_sessions:video_sessions', session_num = 9, video_num = 1, session_announced = 0, english=english)
    else:
        if en:
            form = CategoriesForm_en()
        else:
            form = CategoriesForm()

    context = {
        'form':form,
    }
    return render(request, 'categories.html',context)
