# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20170915_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lane',
            name='project',
        ),
        migrations.AddField(
            model_name='flowcell',
            name='project',
            field=models.ForeignKey(to='management.Project', default=1),
            preserve_default=False,
        ),
    ]
