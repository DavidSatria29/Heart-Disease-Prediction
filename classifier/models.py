from django.db import models

# Create your models here.
class Model(models.Model):
    title = models.CharField(max_length=50, unique=True)
    file = models.FileField(upload_to='models/')
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    label = models.CharField(max_length=50, null=True, blank=True)
