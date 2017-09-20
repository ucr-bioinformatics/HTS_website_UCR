import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import renderers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route, list_route
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


class FormViewSet(ModelViewSet):
    name = 'Default'
    template_name = 'basic-form.html'

    @list_route(renderer_classes=[renderers.TemplateHTMLRenderer])
    def form(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        name = type(serializer).__name__
        name = name[:len(name) - 10]  # Remove serializer portion from name
        print(name)
        return Response({'serializer': serializer, 'title': name})


class ProjectViewSet(FormViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrAdmin)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Project.objects.all()
        return Project.objects.filter(user=self.request.user)

    # @list_route(methods=['get'])
    # def get_form

    @detail_route(methods=['get'])
    def samples(self, request, pk=None):
        sample_list = Sample.objects.filter(project=self.get_object())
        serializer = SampleSerializer(sample_list, many=True)
        return Response(serializer.data)


class FlowcellViewSet(FormViewSet):
    queryset = Flowcell.objects.all()
    serializer_class = FlowcellSerializer
    # renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    # template_name = "test-form.html"

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


class ManufacturerViewSet(FormViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class KitViewSet(FormViewSet):
    queryset = Kit.objects.all()
    serializer_class = KitSerializer


class IndexViewSet(FormViewSet):
    queryset = Index.objects.all()
    serializer_class = IndexSerializer


class SampleViewSet(FormViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    permission_classes = (IsAuthenticated, IsProjectOwnerOrAdmin)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Sample.objects.all()
        return Sample.objects.filter(project__user=self.request.user)


class LaneViewSet(FormViewSet):
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
