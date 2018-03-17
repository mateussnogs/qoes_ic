from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def index(request):
    request.session.clear()
    context = {
        'session_num_view' : str(8) # até 8 excluso, pq a oitava sessão é a última, e todos assistem
    }
    return render(request, 'index.html', context)
