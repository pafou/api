# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1_mqq', '0002_delete_mqq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mqq',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
