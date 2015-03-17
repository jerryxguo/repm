# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_sales_annual_bonus'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='number_of_year_sales',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
