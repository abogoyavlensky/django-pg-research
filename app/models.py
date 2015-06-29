# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.postgres.fields import ArrayField


class Post(models.Model):
    name = models.CharField(max_length=200)
    tags = ArrayField(models.PositiveIntegerField(), blank=True, null = True)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name