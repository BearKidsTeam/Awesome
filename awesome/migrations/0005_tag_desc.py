# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awesome', '0004_application_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='desc',
            field=models.TextField(default='default desc'),
            preserve_default=False,
        ),
    ]
