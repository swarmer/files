import os

from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.validators import RegexValidator


def get_path(upload, orig_name):
    return upload.url_name

class FileUpload(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, default=None)
    file = models.FileField(upload_to=get_path)
    url_name = models.CharField(
        max_length=1000,
        unique=True,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9\-_][a-zA-Z0-9\-_\.]*$',
                message='Allowed characters are: latin letters, digits, .-_'
            )
        ]
    )

    def __str__(self):
        return "<File '%s'>" % self.url_name


@receiver(post_delete, sender=FileUpload)
def file_post_delete(**kwargs):
    instance = kwargs['instance']
    storage = instance.file.storage
    path = instance.file.path
    storage.delete(path)
