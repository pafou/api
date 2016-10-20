# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1_mqq', '0003_auto_20161020_2021'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mqq',
        ),
    ]
