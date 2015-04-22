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
                ('full_name', models.CharField(max_length=80, unique=True, serialize=False, primary_key=True)),
                ('number', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=50, null=True, blank=True)),
                ('mobile', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Client',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notify_type', models.CharField(default=b'NS', max_length=2, choices=[(b'NS', b'NOTIFY_CONSULTANT'), (b'NA', b'NOTIFY_ADMIN'), (b'N1', b'NOTIFY_CLIENT_LETTER_1'), (b'N2', b'NOTIFY_CLIENT_LETTER_2'), (b'N3', b'NOTIFY_CLIENT_LETTER_3')])),
                ('subject', models.CharField(max_length=100, null=True, blank=True)),
                ('sender', models.CharField(max_length=100, null=True, blank=True)),
                ('cc_list', models.CharField(max_length=500, null=True, blank=True)),
                ('bcc_list', models.CharField(max_length=500, null=True, blank=True)),
                ('receiver', models.CharField(max_length=100, null=True, blank=True)),
                ('template', models.FilePathField(path=b'C:\\workspace\\django\\open\\repm\\templates\\email')),
            ],
            options={
                'verbose_name': 'Notify',
                'verbose_name_plural': 'Notify',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('city', models.CharField(max_length=40, unique=True, serialize=False, primary_key=True)),
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
                ('name', models.CharField(max_length=60, unique=True, serialize=False, primary_key=True)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=40, null=True, blank=True)),
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
                ('lot', models.IntegerField()),
                ('price', models.IntegerField()),
                ('status', models.CharField(default=b'----', max_length=20)),
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
                ('mobile', models.CharField(max_length=20)),
                ('start_date', models.DateField(default=datetime.datetime(2015, 4, 22, 7, 20, 15, 351000, tzinfo=utc), null=True, blank=True)),
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
