# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150731_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='url_name',
            field=models.CharField(unique=True, max_length=1000, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z0-9\\-_\\.]+$', message='Allowed characters are: latin letters, digits, .-_')]),
        ),
    ]
