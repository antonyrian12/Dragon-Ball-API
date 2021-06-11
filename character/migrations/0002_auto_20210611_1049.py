# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='fighting_power',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='saga_id',
            field=models.ForeignKey(related_name='saga_character', to='sagas.saga'),
        ),
    ]
