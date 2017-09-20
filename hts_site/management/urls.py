# from management import views
from django.conf.urls import include, url
from rest_framework import routers
from management import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'flowcells', views.FlowcellViewSet)
router.register(r'manufacturers', views.ManufacturerViewSet)
router.register(r'kits', views.KitViewSet)
router.register(r'indexes', views.IndexViewSet)
router.register(r'samples', views.SampleViewSet)
router.register(r'lanes', views.LaneViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^test', views.test),
]
