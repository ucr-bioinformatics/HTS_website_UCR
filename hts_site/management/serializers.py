from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from django.contrib.auth.models import User
from management import models


class ProjectSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.Project
        fields = ('id', 'user', 'title', 'date', 'time', 'status', 'name', 'email',
                  'phone', 'pi', 'billing_account', 'department')


class ProjectField(PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context['request'].user
        if user.is_staff:
            return models.Project.objects.all()
        else:
            return models.Project.objects.filter(user=user)


class FlowcellSerializer(ModelSerializer):
    project = ProjectField()

    class Meta:
        model = models.Flowcell
        fields = ('id', 'project', 'label', 'status', 'date', 'time', 'qc_url')


class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ('id', 'name')


class KitSerializer(ModelSerializer):
    class Meta:
        model = models.Kit
        fields = ('id', 'manufacturer', 'name')


class IndexSerializer(ModelSerializer):
    class Meta:
        model = models.Index
        fields = ('id', 'kit', 'name')


class SampleSerializer(ModelSerializer):
    project = ProjectField()

    class Meta:
        model = models.Sample
        fields = ('id', 'project', 'label', 'project_description', 'organism', 'sequencer', 'alignment_genome',
                  'sample_type', 'dna_conc_ul', 'determined_by', 'dna_conc_ul', 'avg_len_lib',
                  'sample_vol', 'read_length', 'kit', 'kit_other', 'index_type', 'comments',
                  'other_variables', 'sequence_url', 'quality_url', 'status',)


class FlowcellField(PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context['request'].user
        if user.is_staff:
            return models.Flowcell.objects.all()
        else:
            return models.Flowcell.objects.filter(project__user=user)


class LaneSerializer(ModelSerializer):
    flowcell = FlowcellField()

    class Meta:
        model = models.Lane
        fields = ('id', 'flowcell', 'flowcell_element_control', 'flowcell_element_concentration')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login')
