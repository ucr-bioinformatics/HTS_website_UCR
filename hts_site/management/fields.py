from rest_framework.serializers import PrimaryKeyRelatedField
from management import models


class ProjectField(PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context['request'].user
        if user.is_staff:
            return models.Project.objects.all()
        return models.Project.objects.filter(user=user)


class SampleField(PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context['request'].user
        if user.is_staff:
            return models.Sample.objects.all()
        return models.Sample.objects.filter(project__user=user)
