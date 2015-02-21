# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20150214_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deposit', models.IntegerField(default=0)),
                ('solicitor', models.CharField(max_length=40)),
                ('date_of_EOI_sent', models.DateTimeField(default=datetime.datetime(2015, 2, 14, 10, 1, 7, 235000, tzinfo=utc), blank=True)),
                ('date_of_contract_received', models.DateTimeField(default=datetime.datetime(2015, 2, 14, 10, 1, 7, 235000, tzinfo=utc), blank=True)),
                ('date_of_contract_signed', models.DateTimeField(default=datetime.datetime(2015, 2, 14, 10, 1, 7, 235000, tzinfo=utc), blank=True)),
                ('date_of_BOD_paid', models.DateTimeField(default=datetime.datetime(2015, 2, 14, 10, 1, 7, 235000, tzinfo=utc), blank=True)),
                ('date_of_contract_exchanged', models.DateTimeField(default=datetime.datetime(2015, 2, 14, 10, 1, 7, 235000, tzinfo=utc), blank=True)),
                ('date_of_settlement', models.DateTimeField(default=datetime.datetime(2015, 2, 14, 10, 1, 7, 235000, tzinfo=utc), blank=True)),
                ('commission1', models.IntegerField(default=0)),
                ('commission2', models.IntegerField(default=0)),
                ('tyler_commission1', models.IntegerField(default=0)),
                ('tyler_commission2', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=75)),
                ('note', models.CharField(max_length=100)),
                ('letter1', models.CharField(max_length=40)),
                ('letter2', models.CharField(max_length=40)),
                ('letter3', models.CharField(max_length=40)),
                ('client', models.ForeignKey(blank=True, to='sales.Client', null=True)),
                ('office', models.ForeignKey(blank=True, to='sales.Office', null=True)),
                ('project', models.ForeignKey(blank=True, to='sales.Project', null=True)),
                ('property', smart_selects.db_fields.ChainedForeignKey(blank=True, to='sales.Property', null=True)),
                ('sales', smart_selects.db_fields.ChainedForeignKey(blank=True, to='sales.Sales', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='item',
            name='client',
        ),
        migrations.RemoveField(
            model_name='item',
            name='office',
        ),
        migrations.RemoveField(
            model_name='item',
            name='project',
        ),
        migrations.RemoveField(
            model_name='item',
            name='property',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sales',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
