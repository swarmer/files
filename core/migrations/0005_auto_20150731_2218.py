# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_fileupload_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='url_name',
            field=models.SlugField(max_length=1000, unique=True),
        ),
    ]
