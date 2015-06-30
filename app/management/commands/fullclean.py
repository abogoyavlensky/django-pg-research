# -*- coding: utf-8 -*-

from random_words import RandomWords

from django.core.management.base import BaseCommand

from app.models import Tag
from app.models import Post


class Command(BaseCommand):

    def handle(self, *args, **options):
        models = [Tag, Post]
        for model in models:
            model.objects.all().delete()