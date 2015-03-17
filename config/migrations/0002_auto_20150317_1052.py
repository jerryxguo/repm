# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='bonus',
        ),
        migrations.AddField(
            model_name='bonus',
            name='sales',
            field=models.ForeignKey(default='sales', to='config.Sales'),
            preserve_default=False,
        ),
    ]
