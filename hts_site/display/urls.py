from django.conf.urls import url
from display import views


urlpatterns = [
    url(r'^flowcells$', views.flowcells),
    url(r'^projects$', views.projects),
    url(r'', views.index),
]
