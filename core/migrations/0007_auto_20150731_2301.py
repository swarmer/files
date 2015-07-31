# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150731_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='url_name',
            field=models.CharField(unique=True, validators=[django.core.validators.RegexValidator(message='Allowed characters are: latin letters, digits, .-_', regex='^[a-zA-Z0-9\\-_][a-zA-Z0-9\\-_\\.]*$')], max_length=1000),
        ),
    ]
