from django.db import models


# Create your models here.

class Note(models.Model):
    body = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)  # handles the logic of created at
    updated_at = models.DateTimeField(auto_now=True)  # handles the logic of updated at

    def __str__(self):
        return self.body[:30]
