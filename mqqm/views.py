from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, 'mqqm/accueil.html', {'date': datetime.now(), 'pig' : "yes man"})
