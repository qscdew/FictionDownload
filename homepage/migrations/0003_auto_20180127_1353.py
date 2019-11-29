# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20180127_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='owner',
            field=models.ForeignKey(default='', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='writer',
            name='owner',
            field=models.ForeignKey(default='', to=settings.AUTH_USER_MODEL),
        ),
    ]
