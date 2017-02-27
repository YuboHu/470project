# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='engaged_people',
            field=models.IntegerField(default=0, verbose_name=b'Engaged people'),
        ),
    ]
