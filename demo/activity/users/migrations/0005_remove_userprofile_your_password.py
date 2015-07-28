# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_your_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='your_password',
        ),
    ]
