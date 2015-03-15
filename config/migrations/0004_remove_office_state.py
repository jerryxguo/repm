# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_auto_20150315_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='state',
        ),
    ]
