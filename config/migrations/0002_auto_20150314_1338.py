# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(unique=True, max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='full_name',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
    ]
