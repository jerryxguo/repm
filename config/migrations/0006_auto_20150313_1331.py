# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_auto_20150313_1308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sales',
            options={'verbose_name_plural': 'Sales'},
        ),
        migrations.AddField(
            model_name='office',
            name='exclude',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='client',
            field=models.ForeignKey(blank=True, to='config.Client', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='sales',
            field=models.ForeignKey(blank=True, to='config.Sales', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sales',
            name='director',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sales',
            name='referrer',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Referer', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='office',
            name='address',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='office',
            name='country',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='office',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Contact Phone Number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='office',
            name='state',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
