# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_auto_20150312_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 12, 9, 25, 47, 843000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='office',
            field=models.ForeignKey(to='config.Office', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='project',
            field=models.ForeignKey(to='config.Project', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='project_lot',
            field=smart_selects.db_fields.ChainedForeignKey(to='config.Property', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='sales',
            field=smart_selects.db_fields.ChainedForeignKey(to='config.Sales', null=True),
            preserve_default=True,
        ),
    ]
