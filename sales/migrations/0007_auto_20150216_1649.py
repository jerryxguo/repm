# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_auto_20150215_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='property',
            new_name='project_lot',
        ),
    ]
