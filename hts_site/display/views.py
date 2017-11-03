from django.shortcuts import render


def index(request):
    return render(request, 'display/index.html')


def flowcells(request):
    return render(request, 'display/flowcells.html')


def projects(request):
    return render(request, 'display/projects.html')
