from django.conf.urls import url
from display import views


urlpatterns = [
    url(r'^flowcells$', views.flowcells),
    url(r'^projects$', views.projects),
    url(r'^project/(?P<project_id>[0-9]+)', views.project),
    url(r'', views.index),
]
