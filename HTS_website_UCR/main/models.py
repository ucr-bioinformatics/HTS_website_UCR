from django.db import models

# Create your models here.
class project(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    title = models.TextField()
    date = models.TextField()
    time = models.TextField()
    status = models.TextField()
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    pi = models.CharField(max_length=500)
    billing_account = models.CharField(max_length=500)
    department = models.CharField(max_length=500)
    
class sample(models.Model):
	id = models.IntegerField(primary_key=True)
	project_id = models.IntegerField()
	label = models.CharField(max_length=500)
	project_description = models.CharField(max_length=500)
	organism = models.CharField(max_length=500)
	sequencer = models.CharField(max_length=500)
	alignment_genome = models.CharField(max_length=500)
	sample_type = models.CharField(max_length=500)
	dna_conc_ul = models.FloatField()
	determined_by = models.CharField(max_length=100)
	dna_conc_ul = models.FloatField()
	avg_len_lib = models.CharField(max_length=50)
	sample_vol = models.FloatField()
	read_length = models.CharField(max_length=50)
	sample_prep_kit = models.IntegerField()
	kit_other = models.CharField(max_length=500)
	index_type = models.TextField()
	comments = models.TextField()
	other_variables = models.TextField()
	sequence_url = models.TextField()
	quality_url = models.TextField()
	status = models.TextField()
    
class flowcell(models.Model):
	id = models.IntegerField(primary_key=True)
	label = models.TextField()
	status = models.TextField()
	date = models.DateField()
	time = models.TimeField()
	qc_url = models.TextField()
	
class mapping(models.Model):
	flowcell_id = models.IntegerField()
	project_id = models.IntegerField()
	sample_id = models.IntegerField()
	flowcell_element_id = models.IntegerField()
	flowcell_element_control = models.IntegerField()
	flowcell_element_conc = models.FloatField()
	

class manufacturer(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=255)
	
class kit(models.Model):
	id = models.IntegerField(primary_key=True)
	mid = models.IntegerField()
	name = models.CharField(max_length=255)
	
class index(models.Model):
	id = models.IntegerField(primary_key=True)
	kid = models.IntegerField()
	name = models.CharField(max_length=255)
	
	