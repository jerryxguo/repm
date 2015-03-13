# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_auto_20150312_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='id',
        ),
        migrations.AddField(
            model_name='office',
            name='phone',
            field=models.CharField(default=0, max_length=20, verbose_name=b'Contact Phone Number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='office',
            name='city',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
