# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0018_auto_20150311_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='commission1',
            new_name='commission_paid',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='commission2',
            new_name='commission_unpaid',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='tyler_commission1',
            new_name='tyler_commission_paid',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='tyler_commission2',
            new_name='tyler_commission_unpaid',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 10, 22, 51, 25, 423000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
