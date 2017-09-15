from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from management import models


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = models.Project
        fields = ('id', 'user_id', 'title', 'date', 'time', 'status', 'name', 'email',
                  'phone', 'pi', 'billing_account', 'department')


class FlowcellSerializer(ModelSerializer):
    class Meta:
        model = models.Flowcell
        fields = ('id', 'label', 'status', 'date', 'time', 'qc_url')


class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ('id', 'name')


class KitSerializer(ModelSerializer):
    class Meta:
        model = models.Kit
        fields = ('id', 'mid', 'name')


class IndexSerializer(ModelSerializer):
    class Meta:
        model = models.Index
        fields = ('id', 'kid', 'name')


class SampleSerializer(ModelSerializer):
    class Meta:
        model = models.Sample
        fields = ('id', 'label', 'project_description', 'organism', 'sequencer', 'alignment_genome',
                  'sample_type', 'dna_conc_ul', 'determined_by', 'dna_conc_ul', 'avg_len_lib',
                  'sample_vol', 'read_length', 'sample_prep_kit', 'kit_other', 'index_type',
                  'comments', 'other_variables', 'sequence_url', 'quality_url', 'status',)


class LaneSerializer(ModelSerializer):
    class Meta:
        model = models.Lane
        fields = ('id', 'flowcell_id', 'project_id', 'flowcell_element_control', 'flowcell_element_concentration')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login')
