from django.db import models


class Users(models.Model):
    # Явное указание наследования обьектов
    objects = models.Manager()

    user_id = models.AutoField(primary_key=True)
    username = models.TextField(max_length=50)
    secret_phrase = models.TextField(max_length=100)
    user_token = models.TextField(max_length=300)
    uuid_saved = models.UUIDField(max_length=100)
