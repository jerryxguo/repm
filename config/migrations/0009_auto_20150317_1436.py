# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0008_auto_20150317_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='plan_type',
            field=models.CharField(default=b'LB', max_length=2, choices=[(b'LB', b'LOYALTY BONUS'), (b'AB', b'ACCUMULATION BONUS')]),
            preserve_default=True,
        ),
    ]
