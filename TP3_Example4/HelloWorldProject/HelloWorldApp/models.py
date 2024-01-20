
from django.db import models

class MyFileModel(models.Model):
    description = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.description
    



class UploadedFile(models.Model):
    description = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.description
    
    @classmethod
    def get_all_files(cls):
        return cls.objects.all()

