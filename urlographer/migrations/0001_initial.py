# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('view', models.CharField(max_length=255)),
                ('options', django_extensions.db.fields.json.JSONField(blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='URLMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('path', models.CharField(max_length=2000)),
                ('force_secure', models.BooleanField(default=True)),
                ('hexdigest', models.CharField(db_index=True, unique=True, max_length=255, blank=True)),
                ('status_code', models.IntegerField(default=200, db_index=True)),
                ('on_sitemap', models.BooleanField(default=True, db_index=True)),
                ('content_map', models.ForeignKey(blank=True, to='urlographer.ContentMap', null=True)),
                ('redirect', models.ForeignKey(related_name='redirects', blank=True, to='urlographer.URLMap', null=True)),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
    ]
