# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20150724_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='city_name',
        ),
        migrations.RemoveField(
            model_name='events',
            name='country_name',
        ),
        migrations.RemoveField(
            model_name='events',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='events',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='events',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='events',
            name='province_name',
        ),
        migrations.RemoveField(
            model_name='events',
            name='street_name',
        ),
        migrations.RemoveField(
            model_name='events',
            name='street_number',
        ),
    ]
