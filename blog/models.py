from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
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

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    timestamp = models.DateTimeField(default=now,blank=True)