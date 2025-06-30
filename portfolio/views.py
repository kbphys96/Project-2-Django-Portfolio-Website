from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def learning(request):
    return render(request, 'portfolio/learning.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
