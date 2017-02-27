# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_events_updatedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='name_public',
            field=models.BooleanField(default=True),
        ),
    ]
