# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_userprofile_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='advan_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_name', models.CharField(max_length=20, null=True, blank=True)),
                ('city_name', models.CharField(max_length=20, null=True, blank=True)),
                ('province_name', models.CharField(max_length=20, null=True, blank=True)),
                ('postal_code', models.CharField(max_length=20, null=True, blank=True)),
                ('country_name', models.CharField(max_length=20, null=True, blank=True)),
                ('isMusic', models.BooleanField(default=False)),
                ('isSpoorts', models.BooleanField(default=False)),
                ('isFood_Drink', models.BooleanField(default=False)),
                ('isParties', models.BooleanField(default=False)),
                ('isArts', models.BooleanField(default=False)),
                ('isBusniess', models.BooleanField(default=False)),
                ('phonenumber', models.CharField(max_length=20)),
                ('gender', models.CharField(default=b'M', max_length=1, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')])),
            ],
        ),
    ]
