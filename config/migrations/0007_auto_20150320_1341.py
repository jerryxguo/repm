# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0006_auto_20150320_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='subject',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='template',
            field=models.FilePathField(path=b'C:\\workspace\\django\\open\\repm\\templates\\email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sales',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 20, 2, 41, 20, 899000, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
    ]
