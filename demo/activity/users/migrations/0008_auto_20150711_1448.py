# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20150711_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='passworddd',
            new_name='password',
        ),
    ]
