from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)


class Message(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField(max_length=125)

    class Meta:
        ordering = ('date_added', )
