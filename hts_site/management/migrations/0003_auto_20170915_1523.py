# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20170911_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='index',
            old_name='kid',
            new_name='kit',
        ),
        migrations.RenameField(
            model_name='kit',
            old_name='mid',
            new_name='manufacturer',
        ),
        migrations.RenameField(
            model_name='lane',
            old_name='flowcell_id',
            new_name='flowcell',
        ),
        migrations.RenameField(
            model_name='lane',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='sample_prep_kit',
            new_name='kit',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='project_id',
            new_name='project',
        ),
    ]
