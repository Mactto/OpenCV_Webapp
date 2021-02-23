from django.db import models

# Create your models here.
class ImageUploadModel(models.Model):
    description = models.TextField()
    document = models.ImageField(upload_to='images/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)
