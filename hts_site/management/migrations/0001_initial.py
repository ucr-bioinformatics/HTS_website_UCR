# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flowcell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.TextField()),
                ('status', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('qc_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Lane',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flowcell_element_control', models.BooleanField()),
                ('flowcell_element_concentration', models.FloatField()),
                ('flowcell_id', models.ForeignKey(to='management.Flowcell')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('title', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.TextField()),
                ('name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=500)),
                ('pi', models.CharField(max_length=500)),
                ('billing_account', models.CharField(max_length=500)),
                ('department', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=500)),
                ('project_description', models.CharField(max_length=500)),
                ('organism', models.CharField(max_length=500)),
                ('sequencer', models.CharField(max_length=500)),
                ('alignment_genome', models.CharField(max_length=500)),
                ('sample_type', models.CharField(max_length=500)),
                ('determined_by', models.CharField(max_length=100)),
                ('dna_conc_ul', models.FloatField()),
                ('avg_len_lib', models.CharField(max_length=50)),
                ('sample_vol', models.FloatField()),
                ('read_length', models.CharField(max_length=50)),
                ('kit_other', models.CharField(max_length=500)),
                ('index_type', models.TextField()),
                ('comments', models.TextField()),
                ('other_variables', models.TextField()),
                ('sequence_url', models.TextField()),
                ('quality_url', models.TextField()),
                ('status', models.TextField()),
                ('project_id', models.ForeignKey(to='management.Project')),
                ('sample_prep_kit', models.ForeignKey(to='management.Kit')),
            ],
        ),
        migrations.AddField(
            model_name='lane',
            name='project_id',
            field=models.ForeignKey(to='management.Project'),
        ),
        migrations.AddField(
            model_name='kit',
            name='mid',
            field=models.ForeignKey(to='management.Manufacturer'),
        ),
        migrations.AddField(
            model_name='index',
            name='kid',
            field=models.ForeignKey(to='management.Kit'),
        ),
    ]
