from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=15)
    slug = models.CharField(max_length=30, default="")
    timestamp = models.DateTimeField(blank=True)
    image= models.ImageField(upload_to="blog",default="")
    fetured = models.CharField(max_length=5, default="False")

    def __str__(self):
        return self.title + ' by ' + self.author