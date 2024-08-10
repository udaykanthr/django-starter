# middleware.py
from django.shortcuts import redirect

class RedirectBasedOnAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("here: ",request.path)
        if request.path == '/':
            if request.user.is_authenticated:
                return redirect('dashboard')
            else:
                print("redirecting to: Home")
                return redirect('home')
        elif request.path in ['/home/', '/dashboard/']:
            return self.get_response(request)
        
        response = self.get_response(request)
        return response
