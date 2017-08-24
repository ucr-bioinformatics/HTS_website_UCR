from django import forms
from django.forms import formset_factory

class ProjectSubmitForm(forms.Form):
    title = forms.CharField(label='Project Title', max_length=100)
    username = forms.CharField(max_length=30)
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(label='Telephone number', max_length=100)
    pi = forms.CharField(label='Principal Investigator', max_length=100)
    billing_account = forms.CharField(label='Billing Account #', max_length=100)
    department = forms.CharField(label='Department', max_length=100)
    date = forms.CharField(label='Date')
    time = forms.CharField(label='Time')
    status = forms.CharField(label='Status')
    
class FlowcellSubmitForm(forms.Form):
    flowcell_title = forms.CharField(label='Flowcell Title/Label (Required)', max_length=100)
    lane = forms.IntegerField(label='Lane/Cell')
    control_lane = forms.CharField(label='Control Lane', max_length=100)
    project = forms.CharField(label='Project', max_length=500)
    sample = forms.IntegerField(label='Sample')
    concentration = forms.FloatField(label='Concentration on Flowcell (pM)')
    
class SampleSubmitForm(forms.Form):
	label = forms.CharField(label= 'Label', max_length=500)
	project_description = forms.CharField(label= 'Project description', max_length=500)
	organism = forms.CharField(label= 'Organism(s)(full scientific name)', max_length=500)
	sequencer = forms.CharField(label='Sequencer and read options', max_length=500)
	alignment_genome = forms.CharField(label='Alignment genome', max_length=500)
	sample_type = forms.CharField(label='Sample Type (RNASeq, DNASeq, small RNA, etc)', max_length=500)
	dna_conc_ul = forms.FloatField(label='DNA Concentration (ng/ul)')
	determined_by = forms.CharField(label='Concentration measured by',max_length=100)
	dna_conc_ul = forms.FloatField(label='DNA concentration')
	avg_len_lib = forms.CharField(label='Average length or size range of library, including adaptors (bp)',max_length=50)
	sample_vol = forms.FloatField(label='Sample Volume submitted (ul)')
	read_length = forms.CharField(max_length=50)
	sample_prep_kit = forms.IntegerField(label='Sample Prep Kit/Barcodes')
	kit_other = forms.CharField(label='Kit or custom library-making protocol used', max_length=500)
	index_type = forms.IntegerField()
	comments = forms.CharField(label='Comments', max_length=500)
	other_variables = forms.CharField()
	sequence_url = forms.CharField()
	quality_url = forms.CharField()
	status = forms.CharField()




