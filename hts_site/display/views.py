from django.shortcuts import render
from management.models import Project


def index(request):
    return render(request, 'display/index.html')


def flowcells(request):
    return render(request, 'display/flowcells.html')


def projects(request):
    return render(request, 'display/projects.html')


def project(request, project_id):
    projectData = Project.objects.get(pk=project_id)
    # print(projectData)
    return render(request, 'display/project.html', {
        "project_id": project_id,
        "project": projectData,
        "has_permission": request.user.is_staff or request.user == projectData.user
    })
