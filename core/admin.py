from django.contrib import admin

from . import models


class FileUploadAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('file', 'url_name')
        return self.readonly_fields

admin.site.register(models.FileUpload, FileUploadAdmin)
