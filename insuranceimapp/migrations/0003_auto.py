# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field sent_messages on 'UserProfile'
        m2m_table_name = db.shorten_name(u'insuranceimapp_userprofile_sent_messages')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'insuranceimapp.userprofile'], null=False)),
            ('message', models.ForeignKey(orm[u'insuranceimapp.message'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'message_id'])


    def backwards(self, orm):
        # Removing M2M table for field sent_messages on 'UserProfile'
        db.delete_table(db.shorten_name(u'insuranceimapp_userprofile_sent_messages'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'insuranceimapp.groupprofile': {
            'Meta': {'object_name': 'GroupProfile'},
            'group': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.Group']", 'unique': 'True'}),
            'group_active': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '31'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members_list': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members_list'", 'default': 'None', 'to': u"orm['insuranceimapp.UserProfile']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'})
        },
        u'insuranceimapp.message': {
            'Meta': {'object_name': 'Message'},
            'content': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '63'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pushed': ('django.db.models.fields.CharField', [], {'default': "'not_pushed'", 'max_length': '15'}),
            'receiver_groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'receiver_groups'", 'default': 'None', 'to': u"orm['insuranceimapp.GroupProfile']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'receiver_users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'receiver_users'", 'default': 'None', 'to': u"orm['insuranceimapp.UserProfile']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['insuranceimapp.UserProfile']", 'null': 'True', 'blank': 'True'})
        },
        u'insuranceimapp.report': {
            'Meta': {'object_name': 'Report'},
            'action': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '63'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'groups_affected': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'groups_affected'", 'default': 'None', 'to': u"orm['insuranceimapp.GroupProfile']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messages_affected': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'groups_affected'", 'default': 'None', 'to': u"orm['insuranceimapp.Message']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'subaction': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '63'}),
            'user_responsible': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['insuranceimapp.UserProfile']", 'null': 'True', 'blank': 'True'}),
            'users_affected': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'users_affected'", 'default': 'None', 'to': u"orm['insuranceimapp.UserProfile']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'})
        },
        u'insuranceimapp.userinterfacetype': {
            'Meta': {'object_name': 'UserInterfaceType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'redirection_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'insuranceimapp.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'contacts_list': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'contacts_list_field'", 'default': 'None', 'to': u"orm['insuranceimapp.UserProfile']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'groups_list': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'groups_list'", 'default': 'None', 'to': u"orm['insuranceimapp.GroupProfile']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phonenumber': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '31'}),
            'phonenumber_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '7'}),
            'read_messages': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'read_messages'", 'default': 'None', 'to': u"orm['insuranceimapp.Message']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'sent_messages': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sent_messages'", 'default': 'None', 'to': u"orm['insuranceimapp.Message']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'unread_messages': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'unread_messages'", 'default': 'None', 'to': u"orm['insuranceimapp.Message']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'user_active': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '31'})
        }
    }

    complete_apps = ['insuranceimapp']