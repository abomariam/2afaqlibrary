
from django.http import HttpResponseRedirect
from django.utils import translation
from django.utils.deprecation import MiddlewareMixin


class LocaleMiddleware(MiddlewareMixin):
    response_redirect_class = HttpResponseRedirect

    def process_request(self, request):

        if request.path.startswith('/admin/'):
            translation.activate('en')
