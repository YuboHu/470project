# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('brief_intro', models.TextField(verbose_name=b'Brief Introduction')),
                ('poster', models.ImageField(upload_to=b'poster_images', blank=True)),
                ('organizer', models.CharField(max_length=200)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phonenumber', models.CharField(max_length=20)),
                ('capacity', models.IntegerField(verbose_name=b'Maximum number of people')),
                ('age_limit', models.IntegerField(verbose_name=b'Age minimum limit')),
                ('ticket', models.URLField()),
                ('description', models.TextField()),
                ('starttime', models.DateTimeField(verbose_name=b'Start time')),
                ('endtime', models.DateTimeField(verbose_name=b'End time')),
                ('music', models.BooleanField(default=False)),
                ('sports', models.BooleanField(default=False)),
                ('food', models.BooleanField(default=False)),
                ('party', models.BooleanField(default=False)),
                ('arts', models.BooleanField(default=False)),
                ('business', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=300)),
                ('pubdate', models.DateTimeField(verbose_name=b'Date published')),
            ],
        ),
        migrations.CreateModel(
            name='EventsCreater',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creater', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('events', models.OneToOneField(to='events.Events')),
            ],
        ),
    ]
