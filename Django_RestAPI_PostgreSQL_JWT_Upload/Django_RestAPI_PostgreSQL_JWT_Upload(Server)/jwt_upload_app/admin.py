from django.contrib import admin
from .models import Documents


# Register your models here.
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'upload_file']


admin.site.register(Documents, DocumentsAdmin)
