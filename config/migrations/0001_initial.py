# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('mobile', models.CharField(max_length=20, blank=True)),
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
                ('country', models.CharField(max_length=20)),
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
                ('project', models.ForeignKey(blank=True, to='config.Project', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=75)),
                ('mobile', models.CharField(max_length=20)),
                ('number_of_sales', models.IntegerField(default=0, null=True)),
                ('accumulation_bonus', models.IntegerField(default=0, null=True)),
                ('bonus_paid', models.IntegerField(default=0, null=True)),
                ('date_of_paid', models.DateField(null=True, blank=True)),
                ('bonus_unpaid', models.IntegerField(default=0, null=True)),
                ('leader', models.BooleanField(default=False)),
                ('office', models.ForeignKey(blank=True, to='config.Office', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
