# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0010_remove_client_number_of_properties'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Properties'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='id',
        ),
        migrations.AlterField(
            model_name='project',
            name='address',
            field=models.CharField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='city',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
    ]
