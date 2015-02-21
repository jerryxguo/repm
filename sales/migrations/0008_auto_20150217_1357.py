# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_auto_20150216_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='solicitor',
            field=models.CharField(max_length=40, blank=True),
            preserve_default=True,
        ),
    ]
