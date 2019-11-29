# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_liuyan'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='length',
            field=models.IntegerField(default=0),
        ),
    ]
