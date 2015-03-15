# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_of_sales', models.IntegerField(default=0, verbose_name=b'Number of Sales')),
                ('bonus', models.IntegerField(default=0, verbose_name=b'Bonus(AUS)')),
            ],
            options={
                'verbose_name': 'Bonue Plan',
                'verbose_name_plural': 'Bonue Plan',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=30)),
                ('number', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=75, blank=True)),
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
                ('exclude', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=40, null=True, blank=True)),
                ('state', models.CharField(max_length=10, null=True, blank=True)),
                ('country', models.CharField(max_length=10, null=True, blank=True)),
                ('phone', models.CharField(max_length=10, null=True, verbose_name=b'Contact Phone Number', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Office',
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
                ('number_of_sales', models.IntegerField(default=0, null=True, blank=True)),
                ('accumulation_bonus', models.IntegerField(default=0, null=True, blank=True)),
                ('bonus_paid', models.IntegerField(default=0, null=True, blank=True)),
                ('date_of_paid', models.DateField(null=True, blank=True)),
                ('leader', models.BooleanField(default=False)),
                ('is_director', models.BooleanField(default=False)),
                ('on_board', models.BooleanField(default=True)),
                ('referrer', models.CharField(max_length=30, null=True, verbose_name=b'Referer', blank=True)),
                ('office', models.ForeignKey(to='config.Office')),
            ],
            options={
                'verbose_name_plural': 'Sales',
            },
            bases=(models.Model,),
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
    ]
