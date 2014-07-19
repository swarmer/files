import os

from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver


def get_path(upload, orig_name):
    name = upload.url_name or orig_name
    return name

class FileUpload(models.Model):
    file = models.FileField(upload_to=get_path)
    url_name = models.CharField(max_length=1000, unique=True)

    def __str__(self):
        return self.url_name


@receiver(post_delete, sender=FileUpload)
def file_post_delete(**kwargs):
    instance = kwargs['instance']
    storage = instance.file.storage
    path = instance.file.path
    storage.delete(path)
