# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awesome', '0005_tag_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='type',
            field=models.CharField(choices=[('0', 'Category'), ('1', 'Descriptive')], max_length=1, default=0),
            preserve_default=False,
        ),
    ]
