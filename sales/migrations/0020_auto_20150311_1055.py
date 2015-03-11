# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0019_auto_20150311_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='commission_paid',
            new_name='commission_1',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='commission_unpaid',
            new_name='commission_2',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='tyler_commission_paid',
            new_name='tyler_commission_1',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='tyler_commission_unpaid',
            new_name='tyler_commission_2',
        ),
        migrations.AddField(
            model_name='purchase',
            name='commisionn_1_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='commisionn_2_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 10, 23, 55, 50, 689000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
