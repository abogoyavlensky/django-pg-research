# -*- coding: utf-8 -*-

import random

from random_words import RandomWords
from random_words import LoremIpsum

from django.core.management.base import BaseCommand

from app.models import Tag
from app.models import Post


class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()
        self.rw = RandomWords()
        self.li = LoremIpsum()
        self.array_size = 20

    def handle(self, *args, **options):
        tags = []
        for i in xrange(100):
            name = self.rw.random_word().capitalize()
            tag, created = Tag.objects.get_or_create(name=name)
            if created:
                tags.append(tag)
        print '{0} tags has been created.'.format(len(tags))

        posts = []
        tags_ids = Tag.objects.all().values_list('id', flat=True)
        if self.array_size < len(tags_ids):
            for i in xrange(10):
                name = self.rw.random_word().capitalize()
                rand = random.sample(tags_ids, self.array_size)
                post, created = Post.objects.get_or_create(
                    name=name,
                    tags=rand,
                    description=self.li.get_sentences(5),
                )
                if created:
                    posts.append(post)
            print '{0} posts has been created.'.format(len(posts))

        else:
            print 'Please generate more tags than {0}.'.format(self.array_size)
