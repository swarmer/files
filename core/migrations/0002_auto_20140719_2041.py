# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='public',
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=models.FileField(upload_to=core.models.get_path),
        ),
    ]
