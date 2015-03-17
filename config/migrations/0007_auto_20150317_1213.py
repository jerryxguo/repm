# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0006_auto_20150317_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='plan_type',
            field=models.CharField(default=b'LB', max_length=2, choices=[(b'LB', b'LOYALTY BONUS'), (b'OB', b'OUTSTANDING BONUS'), (b'AB', b'ACCUMULATION BONUS')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plan',
            name='year',
            field=models.IntegerField(default=2015, max_length=4, choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plan',
            name='number_of_sales',
            field=models.IntegerField(default=0, verbose_name=b'Least Number of Sales'),
            preserve_default=True,
        ),
    ]
