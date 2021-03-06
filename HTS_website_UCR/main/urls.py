from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects_and_flowcells/',views.projects_flowcells, name='projects_flowcells'),
    url(r'^news/',views.news, name='news'),
    url(r'^protocols/',views.protocols, name='protocols'),
    url(r'^data_analysis/', views.data_analysis, name='data_analysis'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^submit_samples/', views.submit_samples, name='submit_samples'),
    url(r'^workshops/', views.workshops, name='workshops'),
    url(r'^rates/', views.rates, name='rates'),
    url(r'^projects/',views.get_project, name='get_project'),
    url(r'^projects_and_flowcells_submit/',views.get_projects_flowcells, name='get_projects_flowcells'),
    ]
