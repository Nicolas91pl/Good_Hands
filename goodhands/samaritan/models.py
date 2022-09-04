from django.db import models

class Category(models.Model):
    id = models.BigAutoField()
    name = models.CharField(max_length=60, unique=True)
