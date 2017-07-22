from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name