# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('public', models.BooleanField(default=False)),
                ('url_name', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
