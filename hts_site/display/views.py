from django.shortcuts import render


def test(request):
    return render(request, 'display/test.html')


def flowcells(request):
    return render(request, 'display/flowcells.html')
