from django.db import models

# Create your models here.
class Dataset(models.Model):
    title = models.CharField(max_length=50, unique=True)
    file = models.FileField(upload_to='datasets/')