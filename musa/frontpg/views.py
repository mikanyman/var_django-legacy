from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')
    
def yhteystiedot(request):
    return render_to_response('yhteystiedot.html')

def audio(request):
    return render_to_response('audio.html')
    
def styrman(request):
    return render_to_response('styrman.html')

def bio(request):
    return render_to_response('bio.html')