# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20150317_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bonus',
            name='sales',
        ),
        migrations.DeleteModel(
            name='Bonus',
        ),
        migrations.AddField(
            model_name='sales',
            name='accumulation_bonus',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sales',
            name='bonus_paid',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sales',
            name='date_of_paid',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
