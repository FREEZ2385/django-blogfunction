from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    blog_title = models.CharField(max_length = 50)
    blog_subtitle = models.CharField(max_length = 100)
    blog_contents = models.TextField()
    blog_time = models.DateTimeField()
    blog_num = models.AutoField(primary_key = True)

    def __str__(self):
        return self.blog_title



    class Meta:
        ordering = ['-blog_time']
