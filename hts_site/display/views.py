from django.shortcuts import render
from management.models import Project, Flowcell, Sample
import logging

logger = logging.getLogger('django')


def index(request):
    if request.user.is_authenticated():
        return render(request, 'display/index.html')
    return render(request, 'display/unauthenticated.html')


def flowcells(request):
    return render(request, 'display/flowcells.html')


def projects(request):
    return render(request, 'display/projects.html')


def samples(request):
    return render(request, 'display/samples.html')


def unauthorized(request, data_type):
    return render(request, '/display/unauthorized.html', {
        "data_type": data_type
    })


def sample(request, sample_id):
    if not request.user.is_authenticated():
        return unauthorized(request, 'Sample')
    try:
        sampleData = Sample.objects.get(pk=sample_id)
        # print(sampleData)
        if request.user.is_staff or request.user == sampleData.project__user:
            return render(request, 'display/sample.html', {
                "sample_id": sample_id,
                "sample": sampleData
            })
    except Project.DoesNotExist:
        logger.debug('Failed request for project {}'.format(sample_id))
    return unauthorized(request, 'Sample')


def project(request, project_id):
    if not request.user.is_authenticated():
        return unauthorized(request, 'Project')
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
    if not request.user.is_authenticated():
        return unauthorized(request, 'Flowcell')
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
