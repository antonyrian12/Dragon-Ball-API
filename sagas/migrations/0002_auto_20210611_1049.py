# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sagas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saga',
            name='ds_saga',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='saga',
            name='img_saga',
            field=models.CharField(max_length=1500),
        ),
    ]
