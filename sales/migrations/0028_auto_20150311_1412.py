# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0027_auto_20150311_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='last_name',
        ),
        migrations.AddField(
            model_name='client',
            name='full_name',
            field=models.CharField(default='fuyll', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='office',
            name='country',
            field=models.CharField(default='AU', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sales',
            name='full_name',
            field=models.CharField(default='full', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 11, 3, 11, 55, 4000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
