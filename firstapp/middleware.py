from django.shortcuts import redirect
from django.urls import reverse

class RestrictGuestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            restricted_urls = [reverse('login'), reverse('signup')]  # Replace 'login' and 'signup' with your actual URL names
            if request.path in restricted_urls:
                return redirect('home')  # Replace 'home' with the URL where you want to redirect guest users
        return self.get_response(request)






