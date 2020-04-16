from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    image_title = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.image_title

