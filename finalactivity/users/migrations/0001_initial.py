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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birthday', models.DateField()),
                ('make_public_your_user_name', models.BooleanField(default=True)),
                ('street_number', models.CharField(max_length=20, null=True, blank=True)),
                ('street_name', models.CharField(max_length=20, null=True, blank=True)),
                ('city_name', models.CharField(max_length=20, null=True, blank=True)),
                ('province_name', models.CharField(max_length=20, null=True, blank=True)),
                ('postal_code', models.CharField(max_length=20, null=True, blank=True)),
                ('country_name', models.CharField(max_length=20, null=True, blank=True)),
                ('latitude', models.CharField(max_length=20, null=True, blank=True)),
                ('longitude', models.CharField(max_length=20, null=True, blank=True)),
                ('isMusic', models.BooleanField(default=False)),
                ('isSports', models.BooleanField(default=False)),
                ('isFood_Drink', models.BooleanField(default=False)),
                ('isParties', models.BooleanField(default=False)),
                ('isArts', models.BooleanField(default=False)),
                ('isBusiness', models.BooleanField(default=False)),
                ('phonenumber', models.CharField(max_length=20, null=True, blank=True)),
                ('isMale', models.BooleanField(default=True)),
                ('isFemale', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
