from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(max_length=500)

