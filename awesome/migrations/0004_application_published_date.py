# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awesome', '0003_application_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
