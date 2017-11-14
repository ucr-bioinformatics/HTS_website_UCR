from django.shortcuts import render
from management.models import Project, Flowcell
import logging

logger = logging.getLogger('django')


def index(request):
    return render(request, 'display/index.html')


def flowcells(request):
    return render(request, 'display/flowcells.html')


def projects(request):
    return render(request, 'display/projects.html')


def unauthorized(request, data_type):
    return render(request, '/display/unauthorized.html', {
        "data_type": data_type
    })


def project(request, project_id):
    try:
        projectData = Project.objects.get(pk=project_id)
        # print(projectData)
        if request.user.is_staff or request.user == projectData.user:
            return render(request, 'display/project.html', {
                "project_id": project_id,
                "project": projectData
            })
    except Project.DoesNotExist:
        logger.debug('Failed request for project {}'.format(project_id))
    return unauthorized(request, 'Project')


def flowcell(request, fc_id):
    try:
        flowcellData = Flowcell.objects.get(pk=fc_id)
        if request.user.is_staff or request.user == flowcellData.user:
            return render(request, 'display/flowcell.html', {
                "flowcell_id": fc_id,
                "flowcell": flowcellData
            })
    except Flowcell.DoesNotExist:
        logger.debug('Failed request for flowcell {}'.format(fc_id))
    return unauthorized(request, 'Flowcell')
