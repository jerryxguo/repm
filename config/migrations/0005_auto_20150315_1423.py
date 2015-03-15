# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_remove_office_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='office',
            old_name='exclude',
            new_name='indpendent',
        ),
    ]
