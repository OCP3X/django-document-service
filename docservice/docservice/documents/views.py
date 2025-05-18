from django.shortcuts import render

# Create your views here.
import os
from django.http import FileResponse
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Document
from .serializers import DocumentSerializer

class DocumentListCreateView(APIView):
    def get(self, request):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Crear documento con metadatos extraídos del archivo
        document = Document(
            file=file_obj,
            name=file_obj.name,
            size=file_obj.size,
            content_type=file_obj.content_type
        )
        document.save()
        
        serializer = DocumentSerializer(document, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DocumentDetailView(APIView):
    def get_object(self, pk):
        try:
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            return None
    
    def get(self, request, pk):
        document = self.get_object(pk)
        if not document:
            return Response({'error': 'Document not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DocumentSerializer(document, context={'request': request})
        return Response(serializer.data)
    
    def delete(self, request, pk):
        document = self.get_object(pk)
        if not document:
            return Response({'error': 'Document not found'}, status=status.HTTP_404_NOT_FOUND)
        
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DocumentDownloadView(APIView):
    def get(self, request, pk):
        try:
            document = Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            return Response({'error': 'Document not found'}, status=status.HTTP_404_NOT_FOUND)
        
        file_path = document.file.path
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=document.name)