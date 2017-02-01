# -*- coding: utf-8 -*-

from coref.fileman.settings import MEDIA_URL

def urls(request):
    return {'fileman_media_url': MEDIA_URL}
