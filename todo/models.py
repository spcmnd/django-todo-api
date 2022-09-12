from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255, default='')
    done = models.BooleanField(default=False)