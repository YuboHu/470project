# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0006_auto_20150726_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.TextField()),
                ('comments_time', models.DateTimeField()),
                ('like_num', models.IntegerField(default=0)),
                ('dislike_num', models.IntegerField(default=0)),
                ('event', models.ForeignKey(to='events.Events')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
