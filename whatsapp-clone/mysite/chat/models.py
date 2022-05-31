from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class ChatModel(models.Model):
    sender=models.CharField(default=None, max_length=1000)
    message = models.CharField(null=True,blank=True,max_length=10000)
    thread_name=models.CharField(null=True,blank=True,max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message