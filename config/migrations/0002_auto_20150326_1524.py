# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 26, 4, 24, 58, 378000, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
    ]