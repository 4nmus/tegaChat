from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Message(models.Model):
    text = models.TextField("Text", max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now)
    rand_id = models.TextField("ID", null=True, blank=True)
    def get_absolute_url(self):
        return reverse('main', kwargs={})
