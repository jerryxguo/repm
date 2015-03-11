# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deposit', models.IntegerField(default=0, null=True)),
                ('solicitor', models.CharField(max_length=40, blank=True)),
                ('date_of_EOI_sent', models.DateField(null=True, verbose_name=b'Date EOI Sent', blank=True)),
                ('date_of_contract_received', models.DateField(null=True, blank=True)),
                ('date_of_contract_signed', models.DateField(null=True, blank=True)),
                ('date_of_contract_exchanged', models.DateField(null=True, blank=True)),
                ('date_of_BOD_paid', models.DateField(null=True, blank=True)),
                ('date_of_contract_unconditional', models.DateField(null=True, blank=True)),
                ('date_of_settlement', models.DateField(null=True, blank=True)),
                ('commission_1', models.IntegerField(default=0, null=True)),
                ('commission_1_date', models.DateField(null=True, blank=True)),
                ('commission_2', models.IntegerField(default=0, null=True)),
                ('commission_2_date', models.DateField(null=True, blank=True)),
                ('tyler_commission_1', models.IntegerField(default=0, null=True)),
                ('tyler_commission_2', models.IntegerField(default=0, null=True)),
                ('tyler_commission_1_date', models.DateField(null=True, blank=True)),
                ('tyler_commission_2_date', models.DateField(null=True, blank=True)),
                ('bonus', models.IntegerField(default=0, null=True)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('note', models.CharField(max_length=100, blank=True)),
                ('letter1', models.CharField(max_length=40, blank=True)),
                ('letter2', models.CharField(max_length=40, blank=True)),
                ('letter3', models.CharField(max_length=40, blank=True)),
                ('modified_date', models.DateTimeField(default=datetime.datetime(2015, 3, 11, 5, 50, 58, 324000, tzinfo=utc), blank=True)),
            ],
            options={
                'ordering': ['-modified_date'],
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='item',
            name='client',
        ),
        migrations.DeleteModel(
            name='Client',
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
            name='sale',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.RemoveField(
            model_name='property',
            name='project',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='office',
        ),
        migrations.DeleteModel(
            name='Office',
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
        migrations.AddField(
            model_name='purchase',
            name='client',
            field=models.ForeignKey(blank=True, to='config.Client', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='office',
            field=models.ForeignKey(blank=True, to='config.Office', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='project',
            field=models.ForeignKey(blank=True, to='config.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='project_lot',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, to='config.Property', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='sales',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, to='config.Sales', null=True),
            preserve_default=True,
        ),
    ]
