# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_events_engaged_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='updatedate',
            field=models.DateTimeField(null=True, verbose_name=b'Date updated'),
        ),
    ]
