# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_auto_20150312_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='id',
        ),
        migrations.AlterField(
            model_name='sales',
            name='full_name',
            field=models.CharField(max_length=40, unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
