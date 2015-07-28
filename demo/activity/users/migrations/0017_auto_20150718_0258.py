# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20150718_0238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='isSpoorts',
            new_name='isSports',
        ),
    ]
