from django.conf.urls import url
from display import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^flowcells/(?P<fc_id>[0-9]+)$', views.flowcell),
    url(r'^flowcells$', login_required(views.flowcells)),
    url(r'^projects/(?P<project_id>[0-9]+)', views.project),
    url(r'^projects$', login_required(views.projects)),
    url(r'^samples/(?P<sample_id>[0-9]+)', views.sample),
    url(r'^samples$', login_required(views.samples)),
    url(r'', views.index),
]
