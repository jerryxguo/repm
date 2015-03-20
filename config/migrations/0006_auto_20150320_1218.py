# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_auto_20150320_1213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name': 'Notify', 'verbose_name_plural': 'Notify'},
        ),
        migrations.AlterField(
            model_name='notification',
            name='template',
            field=models.FilePathField(allow_folders=True, recursive=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sales',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 20, 1, 18, 35, 928000, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
    ]
