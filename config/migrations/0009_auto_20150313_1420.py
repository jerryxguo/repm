# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0008_auto_20150313_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='date',
        ),
        migrations.AlterField(
            model_name='client',
            name='full_name',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='mobile',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='office',
            name='address',
            field=models.CharField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='office',
            name='country',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='office',
            name='phone',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Contact Phone Number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='office',
            name='state',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='address',
            field=models.CharField(max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='city',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.CharField(default=b'--', max_length=2, choices=[(b'--', b'------'), (b'CR', b'Contract Received'), (b'CS', b'Contract Signed'), (b'CE', b'Contract Exchanged'), (b'CU', b'Contract Unconditional'), (b'PS', b'Property Settled')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sales',
            name='full_name',
            field=models.CharField(max_length=30, unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sales',
            name='referrer',
            field=models.CharField(max_length=30, null=True, verbose_name=b'Referer', blank=True),
            preserve_default=True,
        ),
    ]
