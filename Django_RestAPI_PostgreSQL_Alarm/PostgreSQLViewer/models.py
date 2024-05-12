from django.db import models


class Users(models.Model):
    # Явное указание наследования обьектов
    objects = models.Manager()

    user_id = models.AutoField(primary_key=True)
    username = models.TextField(max_length=50)
    status = models.TextField(max_length=50)
    time = models.TextField(max_length=100)

