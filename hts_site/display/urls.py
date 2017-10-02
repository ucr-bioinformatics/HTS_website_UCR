from django.conf.urls import url
from display import views


urlpatterns = [
    url(r'^test', views.test),
    url(r'^flowcells', views.flowcells),
]
