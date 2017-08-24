from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects_and_flowcells/',views.projects_flowcells, name='projects_flowcells'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^projects/',views.get_project, name='get_project'),
    url(r'^projects_and_flowcells_submit/',views.get_projects_flowcells, name='get_projects_flowcells'),
    ]