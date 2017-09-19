import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route
from management.serializers import *
from management.models import *
from management.permissions import IsOwnerOrAdmin, IsProjectOwnerOrAdmin
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
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrAdmin)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Project.objects.all()
        return Project.objects.filter(user=self.request.user)

    @detail_route(methods=['get'])
    def samples(self, request, pk=None):
        sample_list = Sample.objects.filter(project=self.get_object())
        serializer = SampleSerializer(sample_list, many=True)
        return Response(serializer.data)


class FlowcellViewSet(ModelViewSet):
    queryset = Flowcell.objects.all()
    serializer_class = FlowcellSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Flowcell.objects.all()
        return [lane.flowcell for lane in
                self.request.user.lane_set.all().select_related('flowcell')]

    @detail_route(methods=['get'])
    def lanes(self, request, pk=None):
        lane_list = Lane.objects.filter(flowcell=self.get_object())
        serializer = LaneSerializer(lane_list, many=True)
        return Response(serializer.data)


class ManufacturerViewSet(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class KitViewSet(ModelViewSet):
    queryset = Kit.objects.all()
    serializer_class = KitSerializer


class IndexViewSet(ModelViewSet):
    queryset = Index.objects.all()
    serializer_class = IndexSerializer


class SampleViewSet(ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    permission_classes = (IsAuthenticated, IsProjectOwnerOrAdmin)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Sample.objects.all()
        return Sample.objects.filter(project__user=self.request.user)


class LaneViewSet(ModelViewSet):
    queryset = Lane.objects.all()
    serializer_class = LaneSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Lane.objects.all()
        return Lane.objects.filter(user=self.request.user)



class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
