# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='username',
        ),
        migrations.AddField(
            model_name='project',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
