from management import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.test),
    url(r'^test', views.test),
]
