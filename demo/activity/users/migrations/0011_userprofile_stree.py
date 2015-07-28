# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_advan_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='stree',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
