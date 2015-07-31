from django.contrib import admin

from .models import FileUpload


class FileUploadAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        return {'owner': request.user}

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['file', 'url_name', 'owner']
        else:
            return ['file', 'url_name']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('file', 'url_name')
        return self.readonly_fields

    def has_change_permission(self, request, obj=None):
        has_class_permission = super().has_change_permission(request, obj)
        if not has_class_permission:
            return False

        if obj is None:
            return True

        owns_object = request.user.id == obj.owner.id
        if request.user.is_superuser or owns_object:
            return True

        return False

    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return FileUpload.objects.all()
        return FileUpload.objects.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        obj.save()


admin.site.register(FileUpload, FileUploadAdmin)
