# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_of_sales', models.IntegerField(default=0, null=True, blank=True)),
                ('bonus', models.EmailField(max_length=75, blank=True)),
            ],
            options={
                'verbose_name': 'Bonue Plan',
                'verbose_name_plural': 'Bonue Plan',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name_plural': 'Clients'},
        ),
        migrations.RemoveField(
            model_name='sales',
            name='bonus_unpaid',
        ),
        migrations.AddField(
            model_name='sales',
            name='on_board',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sales',
            name='accumulation_bonus',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sales',
            name='bonus_paid',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sales',
            name='number_of_sales',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
