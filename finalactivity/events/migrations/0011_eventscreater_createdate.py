# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_comments_name_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventscreater',
            name='createdate',
            field=models.DateTimeField(null=True, verbose_name=b'Date published'),
        ),
    ]
