from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html', {'data':'data'})


def secret(request):
    return render(request, 'core/secret.html', {'data':'data'})    