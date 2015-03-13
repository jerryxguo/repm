# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0007_auto_20150313_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='number_of_properties',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='status',
            field=models.CharField(default='--', max_length=2, choices=[(b'CR', b'Contract Received'), (b'CS', b'Contract Signed'), (b'CE', b'Contract Exchanged'), (b'CU', b'Contract Unconditional'), (b'PS', b'Property Settled')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sales',
            name='mobile',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
