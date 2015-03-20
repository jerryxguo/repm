# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_auto_20150319_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notify_type', models.CharField(default=b'NC', max_length=2, choices=[(b'NC', b'NOTIFY_CONSULTANT'), (b'NA', b'NOTIFY_ADMIN'), (b'NC', b'NOTIFY_CLIENT')])),
                ('sender', models.CharField(max_length=30, null=True, blank=True)),
                ('cc_list', models.CharField(max_length=200, null=True, blank=True)),
                ('bcc_list', models.CharField(max_length=200, null=True, blank=True)),
                ('template', models.FilePathField()),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notification',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='sales',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 20, 1, 13, 17, 620000, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
    ]
