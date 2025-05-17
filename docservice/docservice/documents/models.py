from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to="documents/")
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    size = models.PositiveIntegerField()
    content_type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
