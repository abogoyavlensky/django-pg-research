# -*- coding: utf-8 -*-

from django.contrib import admin

from app.models import Post
from app.models import Tag


admin.site.register(Post)
admin.site.register(Tag)
