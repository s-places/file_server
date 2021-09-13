from django.db import models

"""Django models"""
from django.db import models


class File(models.Model):

    objects = models.Manager()
    
    class Meta:
        verbose_name = "File"

    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='')
