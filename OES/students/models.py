from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.user.username