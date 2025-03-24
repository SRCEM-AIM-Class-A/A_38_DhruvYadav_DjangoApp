from django.shortcuts import render

def sample(request):
    return render(request, 'sample.html')  # This refers to templates/sample.html
