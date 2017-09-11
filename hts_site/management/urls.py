# from management import views
from django.conf.urls import include, url
from rest_framework import routers
from management import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'samples', views.SampleViewSet)
router.register(r'projects', views.ProjectViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
