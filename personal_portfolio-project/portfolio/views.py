from django.shortcuts import render, get_object_or_404
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})


def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects':projects})


