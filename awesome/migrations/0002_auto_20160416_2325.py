# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awesome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('app_type', models.CharField(max_length=1, choices=[('0', 'Game'), ('1', 'Software')])),
                ('name', models.CharField(max_length=200)),
                ('steam_appid', models.IntegerField()),
                ('is_free', models.NullBooleanField()),
                ('header_img', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='tags',
            field=models.ManyToManyField(to='awesome.Tag'),
        ),
    ]
