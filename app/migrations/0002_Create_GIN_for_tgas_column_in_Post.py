# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""CREATE INDEX idx_test on "app_post" USING GIN ("tags");"""),
        migrations.RunSQL("SET enable_seqscan TO off;"),
    ]
