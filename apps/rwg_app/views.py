from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    # print(request.session)
    if 'word' not in request.session:
        request.session['count'] = 0
        # print(request.session)
    return render(request, 'rwg_app/index.html')

def random_word(request):
    request.session['count'] +=1
    request.session['word'] = get_random_string(length=14)
    print(request.session['word'])
    return redirect('/')

def reset(request):
    # This clears the entire session. Both word and count.
    request.session.clear()
    # del request.session['word']...also works but specifically 
    # deletes word session and brings the count back to 0, at the top.
    # del request.session['word']
    return redirect('/')