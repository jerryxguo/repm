# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_auto_20150315_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='office',
            old_name='indpendent',
            new_name='independent',
        ),
    ]
