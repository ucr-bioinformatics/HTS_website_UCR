# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20170918_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flowcell',
            name='project',
        ),
        migrations.AddField(
            model_name='lane',
            name='sample',
            field=models.ForeignKey(default=1, to='management.Sample'),
            preserve_default=False,
        ),
    ]
