# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20150312_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonus',
            name='bonus',
            field=models.IntegerField(default=0, verbose_name=b'Bonus(AUS)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bonus',
            name='number_of_sales',
            field=models.IntegerField(default=0, verbose_name=b'Number of Sales'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sales',
            name='full_name',
            field=models.CharField(unique=True, max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sales',
            name='on_board',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
