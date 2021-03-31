from django.db import models
from django.urls import reverse


class Member(models.Model):
    username = models.CharField(max_length=120)
    
    def get_absolute_url(self):
        return reverse("hello:member_details")
