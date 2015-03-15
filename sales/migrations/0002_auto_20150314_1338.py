# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='client',
            field=models.ForeignKey(to='config.Client', to_field=b'full_name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='client_email',
            field=models.ForeignKey(related_name='mail', to='config.Client', to_field=b'email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 14, 2, 38, 35, 918000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
