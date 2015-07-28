# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_userprofile_stree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advan_user',
            name='phonenumber',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
