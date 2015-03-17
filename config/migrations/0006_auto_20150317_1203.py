# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_sales_number_of_year_sales'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='annual_bonus',
            new_name='year_bonus',
        ),
    ]
