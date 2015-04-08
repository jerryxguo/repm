# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
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
                ('commission_1', models.IntegerField(default=0, null=True, blank=True)),
                ('commission_1_date', models.DateField(null=True, blank=True)),
                ('commission_2', models.IntegerField(default=0, null=True, blank=True)),
                ('commission_2_date', models.DateField(null=True, blank=True)),
                ('tyler_commission_1', models.IntegerField(default=0, null=True, blank=True)),
                ('tyler_commission_2', models.IntegerField(default=0, null=True, blank=True)),
                ('tyler_commission_1_date', models.DateField(null=True, blank=True)),
                ('tyler_commission_2_date', models.DateField(null=True, blank=True)),
                ('bonus', models.IntegerField(default=0, null=True, blank=True)),
                ('note', models.CharField(max_length=100, blank=True)),
                ('letter1', models.BooleanField(default=False)),
                ('letter2', models.BooleanField(default=False)),
                ('letter3', models.BooleanField(default=False)),
                ('modified_date', models.DateTimeField(default=datetime.datetime(2015, 3, 26, 4, 24, 42, 311000, tzinfo=utc), blank=True)),
                ('lot_price', models.IntegerField(default=0, null=True)),
                ('client', models.ForeignKey(to='config.Client', to_field=b'full_name')),
                ('office', models.ForeignKey(to='config.Office')),
                ('project', models.ForeignKey(to='config.Project')),
                ('project_lot', smart_selects.db_fields.ChainedForeignKey(to='config.Property')),
                ('sales', smart_selects.db_fields.ChainedForeignKey(to='config.Sales')),
            ],
            options={
                'ordering': ['-modified_date'],
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sale Records',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='purchase',
            unique_together=set([('project', 'project_lot')]),
        ),
    ]
