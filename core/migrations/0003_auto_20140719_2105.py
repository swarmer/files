# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20140719_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='url_name',
            field=models.CharField(unique=True, max_length=1000),
        ),
    ]
