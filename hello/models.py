from django.db import models


class Member(models.Model):
    username = models.CharField(max_length=120)
