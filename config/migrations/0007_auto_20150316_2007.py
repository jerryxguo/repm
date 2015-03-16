# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0006_auto_20150315_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='start_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='office',
            name='phone',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Contact Phone', blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='property',
            unique_together=set([('project', 'lot')]),
        ),
        migrations.AlterUniqueTogether(
            name='sales',
            unique_together=set([('office', 'full_name')]),
        ),
    ]
