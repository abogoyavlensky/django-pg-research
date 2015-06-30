# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.postgres.fields import ArrayField


class Post(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    tags = ArrayField(models.PositiveIntegerField(), blank=True, null = True)

    def __unicode__(self):
        return '{0} Id: {1}'.format(self.name, self.id)


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return '{0} Id: {1}'.format(self.name, self.id)