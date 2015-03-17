# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0007_auto_20150317_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='year',
            field=models.IntegerField(default=None, max_length=4, null=True, blank=True, choices=[(2015, 2015), (2016, 2016)]),
            preserve_default=True,
        ),
    ]
