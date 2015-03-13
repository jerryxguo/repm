# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0006_auto_20150313_1331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name_plural': 'Client'},
        ),
        migrations.AlterModelOptions(
            name='office',
            options={'verbose_name_plural': 'Office'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name_plural': 'project'},
        ),
        migrations.RenameField(
            model_name='sales',
            old_name='director',
            new_name='is_director',
        ),
    ]
