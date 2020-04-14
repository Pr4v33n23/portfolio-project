from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_pub_date = models.DateTimeField()
    blog_body = models.TextField()
    blog_image = models.ImageField(upload_to='blogs/')