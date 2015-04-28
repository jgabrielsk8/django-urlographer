# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ContentMap.created'
        db.add_column(u'urlographer_contentmap', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'ContentMap.modified'
        db.add_column(u'urlographer_contentmap', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'URLMap.created'
        db.add_column(u'urlographer_urlmap', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'URLMap.modified'
        db.add_column(u'urlographer_urlmap', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ContentMap.created'
        db.delete_column(u'urlographer_contentmap', 'created')

        # Deleting field 'ContentMap.modified'
        db.delete_column(u'urlographer_contentmap', 'modified')

        # Deleting field 'URLMap.created'
        db.delete_column(u'urlographer_urlmap', 'created')

        # Deleting field 'URLMap.modified'
        db.delete_column(u'urlographer_urlmap', 'modified')


    models = {
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'urlographer.contentmap': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'ContentMap'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'options': ('django.db.models.fields.TextField', [], {'default': "'{}'", 'blank': 'True'}),
            'view': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'urlographer.urlmap': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'URLMap'},
            'content_map': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['urlographer.ContentMap']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'force_secure': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hexdigest': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'on_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'redirect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'redirects'", 'null': 'True', 'to': u"orm['urlographer.URLMap']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'status_code': ('django.db.models.fields.IntegerField', [], {'default': '200', 'db_index': 'True'})
        }
    }

    complete_apps = ['urlographer']