# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_auto_20150217_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='Last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='sales',
            old_name='Last_name',
            new_name='last_name',
        ),
    ]
