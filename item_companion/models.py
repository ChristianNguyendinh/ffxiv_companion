from __future__ import unicode_literals

from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField(max_length=255, blank=False)
    main_type = models.CharField(max_length=255, blank=False)
    sub_type = models.CharField(max_length=255, blank=False)
    img = models.CharField(max_length=255, blank=False)
    ilvl = models.SmallIntegerField(blank=False)
    rlvl = models.SmallIntegerField(blank=False)

    def __str__(self):
        return self.name
        