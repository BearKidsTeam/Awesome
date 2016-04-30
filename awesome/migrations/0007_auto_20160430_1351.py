# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awesome', '0006_tag_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='assoc',
            field=models.ForeignKey(to='awesome.Application', null=True, default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='type',
            field=models.CharField(max_length=1, choices=[('0', 'Category'), ('1', 'Descriptive'), ('2', 'Platform')]),
        ),
    ]
