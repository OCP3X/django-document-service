from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_at', 'size', 'content_type')
    search_fields = ('name', 'content_type')
    readonly_fields = ('uploaded_at', 'size', 'content_type')