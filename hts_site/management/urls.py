# from management import views
from django.conf.urls import include, url

from rest_framework import routers, serializers, viewsets

from management.models import Sample


# Serializers define the API representation.
class SampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sample
        fields = ('label', 'project_description', 'organism', 'sequencer', 'alignment_genome',
                  'sample_type', 'dna_conc_ul', 'determined_by', 'dna_conc_ul', 'avg_len_lib',
                  'sample_vol', 'read_length', 'sample_prep_kit', 'kit_other', 'index_type',
                  'comments', 'other_variables', 'sequence_url', 'quality_url', 'status',)


# ViewSets define the view behavior.
class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'samples', SampleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
