# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20140719_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='owner',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
