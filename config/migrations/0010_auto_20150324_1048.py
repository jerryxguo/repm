# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0009_auto_20150324_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='bcc_list',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='cc_list',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='sender',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='subject',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sales',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 23, 23, 48, 0, 431000, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
    ]
