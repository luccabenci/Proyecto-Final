from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='user_photos/', blank=True)

    class Meta:
        app_label = 'blog'

class CreateNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='note_images/', blank=True, null=True)

    def __str__(self):
        return self.title
