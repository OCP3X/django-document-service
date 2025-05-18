from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    download_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Document
        fields = ['id', 'name', 'file', 'uploaded_at', 'size', 'content_type', 'download_url']
        read_only_fields = ['uploaded_at', 'size', 'content_type', 'download_url']
    
    def get_download_url(self, obj):
        request = self.context.get('request')
        if request and obj.id:
            return request.build_absolute_uri(f'/documents/{obj.id}/download/')
        return None