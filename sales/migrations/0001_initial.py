# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('Last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75)),
                ('mobile', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deposit', models.IntegerField(default=0)),
                ('solicitor', models.CharField(max_length=40)),
                ('date_of_EOI_sent', models.DateTimeField(default=datetime.datetime(2015, 2, 14, 9, 42, 57, 310000, tzinfo=utc), blank=True)),
                ('date_of_contract_received', models.DateTimeField(default=datetime.datetime(2015, 2, 14, 9, 42, 57, 310000, tzinfo=utc), blank=True)),
                ('date_of_contract_signed', models.DateTimeField(default=datetime.datetime(2015, 2, 14, 9, 42, 57, 310000, tzinfo=utc), blank=True)),
                ('date_of_BOD_paid', models.DateTimeField(default=datetime.datetime(2015, 2, 14, 9, 42, 57, 310000, tzinfo=utc), blank=True)),
                ('date_of_contract_exchanged', models.DateTimeField(default=datetime.datetime(2015, 2, 14, 9, 42, 57, 310000, tzinfo=utc), blank=True)),
                ('date_of_settlement', models.DateTimeField(default=datetime.datetime(2015, 2, 14, 9, 42, 57, 310000, tzinfo=utc), blank=True)),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lot', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('project', models.ForeignKey(blank=True, to='sales.Project', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('Last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75)),
                ('mobile', models.CharField(max_length=20)),
                ('office', models.ForeignKey(blank=True, to='sales.Office', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='office',
            field=models.ForeignKey(blank=True, to='sales.Office', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='project',
            field=models.ForeignKey(blank=True, to='sales.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='property',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, to='sales.Property', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='sale',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, to='sales.Sale', null=True),
            preserve_default=True,
        ),
    ]
