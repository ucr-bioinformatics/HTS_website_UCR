# from management import views
from django.conf.urls import include, url
from rest_framework import routers
from management.views import SampleViewSet, ProjectViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'samples', SampleViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
