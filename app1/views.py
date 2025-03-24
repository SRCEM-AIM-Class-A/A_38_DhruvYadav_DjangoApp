from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # This refers to templates/home.html
