# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0009_auto_20150313_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='number_of_properties',
        ),
    ]
