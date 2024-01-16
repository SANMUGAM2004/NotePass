
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Profile for {self.user.username}'

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.title

class Password(models.Model):
    website = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return f'{self.website} - {self.username}'


