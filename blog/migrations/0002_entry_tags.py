# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20140910_0105'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]