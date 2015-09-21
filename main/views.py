from django.shortcuts import render


def about(request):
    return render(request, 'main/about.html')

def home(request):
    return render(request, 'main/home.html')
