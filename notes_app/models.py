from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User,related_name='notes',on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("notes_app:list_note")
