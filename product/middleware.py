from django.utils.crypto import get_random_string

class AnonymousUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not request.session.get('anonymous_identifier'):
            request.session['anonymous_identifier'] = get_random_string(32)
        response = self.get_response(request)
        return response
