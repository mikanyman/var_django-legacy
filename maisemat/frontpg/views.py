from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


@login_required
def etusivu(request):
    return render_to_response('etusivu.html',
        context_instance=RequestContext(request))

@login_required
def kuvat(request):
    return render_to_response('kuvat.html',
        context_instance=RequestContext(request))

@login_required
def dokumentit(request):
    return render_to_response('dokumentit.html',
        context_instance=RequestContext(request))

@login_required
def kalenteri(request):
    return render_to_response('kalenteri.html',
        context_instance=RequestContext(request))

@login_required
def yhteystiedot(request):
    return render_to_response('yhteystiedot.html',
        context_instance=RequestContext(request))

@login_required
def kieli(request):
    return render_to_response('kieli.html',
        context_instance=RequestContext(request))
