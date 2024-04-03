from django.shortcuts import redirect

class PasswordMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.get('password_entered', False) and request.path != '/password_entry/':
            return redirect('password_entry')
        response = self.get_response(request)
        return response