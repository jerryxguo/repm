# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20150314_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='is_director',
            new_name='director',
        ),
    ]
