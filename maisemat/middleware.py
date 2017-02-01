class SetLangFi(object):
    def process_request(self, request):
        request.session['django_language'] = 'fi'