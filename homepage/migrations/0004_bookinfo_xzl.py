# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20180127_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='xzl',
            field=models.IntegerField(default=0),
        ),
    ]
