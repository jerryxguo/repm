# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
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
                ('full_name', models.CharField(unique=True, max_length=30)),
                ('number', models.IntegerField(default=0)),
                ('email', models.EmailField(unique=True, max_length=75, blank=True)),
                ('mobile', models.CharField(max_length=10, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Client',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('city', models.CharField(max_length=20, unique=True, serialize=False, primary_key=True)),
                ('independent', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=40, null=True, blank=True)),
                ('country', models.CharField(max_length=10, null=True, blank=True)),
                ('phone', models.CharField(max_length=10, null=True, verbose_name=b'Contact Phone', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Office',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan_type', models.CharField(default=b'LB', max_length=2, choices=[(b'LB', b'LOYALTY BONUS'), (b'AB', b'ACCUMULATION BONUS')])),
                ('year', models.IntegerField(default=None, max_length=4, null=True, blank=True, choices=[(2015, 2015), (2016, 2016)])),
                ('number_of_sales', models.IntegerField(default=0, verbose_name=b'Least Number of Sales')),
                ('bonus', models.IntegerField(default=0, verbose_name=b'Bonus(AUS)')),
            ],
            options={
                'verbose_name': 'Bonus Plan',
                'verbose_name_plural': 'Bonus Plan',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('name', models.CharField(max_length=20, unique=True, serialize=False, primary_key=True)),
                ('address', models.CharField(max_length=40, null=True, blank=True)),
                ('city', models.CharField(max_length=10, null=True, blank=True)),
                ('state', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'project',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lot', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('status', models.CharField(default=b'--', max_length=2, choices=[(b'--', b'------'), (b'CR', b'Contract Received'), (b'CS', b'Contract Signed'), (b'CE', b'Contract Exchanged'), (b'CU', b'Contract Unconditional'), (b'PS', b'Property Settled')])),
                ('modification_date', models.DateField(null=True, blank=True)),
                ('lot_client', models.ForeignKey(blank=True, to='config.Client', null=True)),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('full_name', models.CharField(max_length=30, unique=True, serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('mobile', models.CharField(max_length=10)),
                ('start_date', models.DateField(default=datetime.datetime(2015, 3, 19, 0, 33, 26, 26000, tzinfo=utc), null=True, blank=True)),
                ('number_of_year_sales', models.IntegerField(default=0, null=True, blank=True)),
                ('year_bonus', models.IntegerField(default=0, null=True, blank=True)),
                ('number_of_sales', models.IntegerField(default=0, null=True, blank=True)),
                ('accumulation_bonus', models.IntegerField(default=0, null=True, blank=True)),
                ('bonus_paid', models.IntegerField(default=0, null=True, verbose_name=b'Accum bonus paid', blank=True)),
                ('date_of_paid', models.DateField(null=True, blank=True)),
                ('leader', models.BooleanField(default=False)),
                ('director', models.BooleanField(default=False)),
                ('on_board', models.BooleanField(default=True)),
                ('referrer', models.CharField(max_length=30, null=True, verbose_name=b'Referer', blank=True)),
                ('office', models.ForeignKey(to='config.Office')),
            ],
            options={
                'verbose_name': 'Consultant:',
                'verbose_name_plural': 'Consultants',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='sales',
            unique_together=set([('office', 'full_name')]),
        ),
        migrations.AddField(
            model_name='property',
            name='lot_sales',
            field=models.ForeignKey(blank=True, to='config.Sales', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='project',
            field=models.ForeignKey(to='config.Project'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='property',
            unique_together=set([('project', 'lot')]),
        ),
    ]
