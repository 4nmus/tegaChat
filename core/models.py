from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Message(models.Model):
    text = models.TextField("Text", max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)


