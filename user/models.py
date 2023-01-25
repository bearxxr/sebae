from django.db import models


class User(models.Model):
    nickname = models.CharField(verbose_name='昵称', max_length=32)
