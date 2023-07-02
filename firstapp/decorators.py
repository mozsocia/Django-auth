from django.shortcuts import redirect

def auth_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Replace 'login' with your login URL

        return view_func(request, *args, **kwargs)

    return wrapper


def guest_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Replace 'login' with your login URL

        return view_func(request, *args, **kwargs)

    return wrapper
