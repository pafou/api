# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mqq',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('alias', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=3)),
                ('env', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='mqq',
            unique_together=set([('alias', 'env')]),
        ),
    ]
