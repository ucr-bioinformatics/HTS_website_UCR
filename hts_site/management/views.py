import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from management import models
from django.contrib.auth.models import User
from management import serializers, permissions
from rest_framework.permissions import IsAuthenticated
# from django.shortcuts import render


@csrf_exempt
def test(request):
    try:
        if request.method != 'POST':
            return JsonResponse({'status': 'fail'})
        data = json.loads(request.body.decode("utf-8"))
        res = JsonResponse({'status': 'success', 'name': data['name']})
        return res
    except KeyError:
        return JsonResponse({'status': 'fail', 'message': 'Missing field'})
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error'})


class ProjectViewSet(ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = (IsAuthenticated, permissions.IsOwnerOrAdminOrReadOnly)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff:
            return models.Project.objects.all()
        else:
            return models.Project.objects.filter(user=self.request.user)


class FlowcellViewSet(ModelViewSet):
    queryset = models.Flowcell.objects.all()
    serializer_class = serializers.FlowcellSerializer


class ManufacturerViewSet(ModelViewSet):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer


class KitViewSet(ModelViewSet):
    queryset = models.Kit.objects.all()
    serializer_class = serializers.KitSerializer


class IndexViewSet(ModelViewSet):
    queryset = models.Index.objects.all()
    serializer_class = serializers.IndexSerializer


class SampleViewSet(ModelViewSet):
    queryset = models.Sample.objects.all()
    serializer_class = serializers.SampleSerializer


class LaneViewSet(ModelViewSet):
    queryset = models.Lane.objects.all()
    serializer_class = serializers.LaneSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
