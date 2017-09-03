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
    iid = models.CharField(max_length=255, blank=False)
    ilvl = models.SmallIntegerField(blank=False)
    rlvl = models.SmallIntegerField(blank=False)

    def __str__(self):
        return self.name

class Botany_Node(models.Model):
    item = models.CharField(max_length=255, blank=False)
    node_type = models.CharField(max_length=255, blank=False)
    level = models.CharField(max_length=255, blank=False)
    zone = models.CharField(max_length=255, blank=False)
    coords = models.CharField(max_length=255, blank=False)

class Miner_Node(models.Model):
    item = models.CharField(max_length=255, blank=False)
    node_type = models.CharField(max_length=255, blank=False)
    level = models.CharField(max_length=255, blank=False)
    zone = models.CharField(max_length=255, blank=False)
    coords = models.CharField(max_length=255, blank=False)

#    CREATE TABLE "temp" ("item" varchar(255) NOT NULL, "node_type" varchar(255) NOT NULL, "level" varchar(255) NOT NULL, "zone" varchar(255) NOT NULL, "coords" varchar(255) NOT NULL);
        