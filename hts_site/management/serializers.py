from rest_framework import serializers
from django.contrib.auth.models import User
from management.models import Project, Sample


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'user_id', 'title', 'date', 'time', 'status', 'name', 'email',
                  'phone', 'pi', 'billing_account', 'department')


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ('id', 'label', 'project_description', 'organism', 'sequencer', 'alignment_genome',
                  'sample_type', 'dna_conc_ul', 'determined_by', 'dna_conc_ul', 'avg_len_lib',
                  'sample_vol', 'read_length', 'sample_prep_kit', 'kit_other', 'index_type',
                  'comments', 'other_variables', 'sequence_url', 'quality_url', 'status',)
