# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Report'
        db.create_table(u'insuranceimapp_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action', self.gf('django.db.models.fields.CharField')(default='', max_length=63)),
            ('subaction', self.gf('django.db.models.fields.CharField')(default='', max_length=63)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('user_responsible', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User'], null=True, blank=True)),
        ))
        db.send_create_signal(u'insuranceimapp', ['Report'])

        # Adding M2M table for field users_affected on 'Report'
        m2m_table_name = db.shorten_name(u'insuranceimapp_report_users_affected')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('report', models.ForeignKey(orm[u'insuranceimapp.report'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['report_id', 'user_id'])

        # Adding M2M table for field groups_affected on 'Report'
        m2m_table_name = db.shorten_name(u'insuranceimapp_report_groups_affected')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('report', models.ForeignKey(orm[u'insuranceimapp.report'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['report_id', 'group_id'])

        # Adding M2M table for field messages_affected on 'Report'
        m2m_table_name = db.shorten_name(u'insuranceimapp_report_messages_affected')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('report', models.ForeignKey(orm[u'insuranceimapp.report'], null=False)),
            ('message', models.ForeignKey(orm[u'insuranceimapp.message'], null=False))
        ))
        db.create_unique(m2m_table_name, ['report_id', 'message_id'])

        # Adding model 'UserProfile'
        db.create_table(u'insuranceimapp_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('phonenumber_prefix', self.gf('django.db.models.fields.CharField')(default='', max_length=7)),
            ('phonenumber', self.gf('django.db.models.fields.CharField')(default='', max_length=31)),
            ('user_active', self.gf('django.db.models.fields.CharField')(default='active', max_length=31)),
        ))
        db.send_create_signal(u'insuranceimapp', ['UserProfile'])

        # Adding M2M table for field contacts_list on 'UserProfile'
        m2m_table_name = db.shorten_name(u'insuranceimapp_userprofile_contacts_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'insuranceimapp.userprofile'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'user_id'])

        # Adding M2M table for field unread_messages on 'UserProfile'
        m2m_table_name = db.shorten_name(u'insuranceimapp_userprofile_unread_messages')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'insuranceimapp.userprofile'], null=False)),
            ('message', models.ForeignKey(orm[u'insuranceimapp.message'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'message_id'])

        # Adding M2M table for field read_messages on 'UserProfile'
        m2m_table_name = db.shorten_name(u'insuranceimapp_userprofile_read_messages')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'insuranceimapp.userprofile'], null=False)),
            ('message', models.ForeignKey(orm[u'insuranceimapp.message'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'message_id'])

        # Adding model 'GroupProfile'
        db.create_table(u'insuranceimapp_groupprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.Group'], unique=True)),
            ('group_active', self.gf('django.db.models.fields.CharField')(default='active', max_length=31)),
        ))
        db.send_create_signal(u'insuranceimapp', ['GroupProfile'])

        # Adding M2M table for field members_list on 'GroupProfile'
        m2m_table_name = db.shorten_name(u'insuranceimapp_groupprofile_members_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('groupprofile', models.ForeignKey(orm[u'insuranceimapp.groupprofile'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['groupprofile_id', 'user_id'])

        # Adding model 'Message'
        db.create_table(u'insuranceimapp_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(default='', max_length=63)),
            ('pushed', self.gf('django.db.models.fields.CharField')(default='not_pushed', max_length=15)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User'], null=True, blank=True)),
        ))
        db.send_create_signal(u'insuranceimapp', ['Message'])

        # Adding M2M table for field receiver_users on 'Message'
        m2m_table_name = db.shorten_name(u'insuranceimapp_message_receiver_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('message', models.ForeignKey(orm[u'insuranceimapp.message'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['message_id', 'user_id'])

        # Adding M2M table for field receiver_groups on 'Message'
        m2m_table_name = db.shorten_name(u'insuranceimapp_message_receiver_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('message', models.ForeignKey(orm[u'insuranceimapp.message'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['message_id', 'group_id'])

        # Adding model 'UserInterfaceType'
        db.create_table(u'insuranceimapp_userinterfacetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('redirection_url', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal(u'insuranceimapp', ['UserInterfaceType'])


    def backwards(self, orm):
        # Deleting model 'Report'
        db.delete_table(u'insuranceimapp_report')

        # Removing M2M table for field users_affected on 'Report'
        db.delete_table(db.shorten_name(u'insuranceimapp_report_users_affected'))

        # Removing M2M table for field groups_affected on 'Report'
        db.delete_table(db.shorten_name(u'insuranceimapp_report_groups_affected'))

        # Removing M2M table for field messages_affected on 'Report'
        db.delete_table(db.shorten_name(u'insuranceimapp_report_messages_affected'))

        # Deleting model 'UserProfile'
        db.delete_table(u'insuranceimapp_userprofile')

        # Removing M2M table for field contacts_list on 'UserProfile'
        db.delete_table(db.shorten_name(u'insuranceimapp_userprofile_contacts_list'))

        # Removing M2M table for field unread_messages on 'UserProfile'
        db.delete_table(db.shorten_name(u'insuranceimapp_userprofile_unread_messages'))

        # Removing M2M table for field read_messages on 'UserProfile'
        db.delete_table(db.shorten_name(u'insuranceimapp_userprofile_read_messages'))

        # Deleting model 'GroupProfile'
        db.delete_table(u'insuranceimapp_groupprofile')

        # Removing M2M table for field members_list on 'GroupProfile'
        db.delete_table(db.shorten_name(u'insuranceimapp_groupprofile_members_list'))

        # Deleting model 'Message'
        db.delete_table(u'insuranceimapp_message')

        # Removing M2M table for field receiver_users on 'Message'
        db.delete_table(db.shorten_name(u'insuranceimapp_message_receiver_users'))

        # Removing M2M table for field receiver_groups on 'Message'
        db.delete_table(db.shorten_name(u'insuranceimapp_message_receiver_groups'))

        # Deleting model 'UserInterfaceType'
        db.delete_table(u'insuranceimapp_userinterfacetype')


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
            'members_list': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members_list'", 'default': 'None', 'to': u"orm['auth.User']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'})
        },
        u'insuranceimapp.message': {
            'Meta': {'object_name': 'Message'},
            'content': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '63'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pushed': ('django.db.models.fields.CharField', [], {'default': "'not_pushed'", 'max_length': '15'}),
            'receiver_groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'receiver_groups'", 'default': 'None', 'to': u"orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'receiver_users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'receiver_users'", 'default': 'None', 'to': u"orm['auth.User']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'insuranceimapp.report': {
            'Meta': {'object_name': 'Report'},
            'action': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '63'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'groups_affected': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'groups_affected'", 'default': 'None', 'to': u"orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messages_affected': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'groups_affected'", 'default': 'None', 'to': u"orm['insuranceimapp.Message']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'subaction': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '63'}),
            'user_responsible': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'users_affected': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'users_affected'", 'default': 'None', 'to': u"orm['auth.User']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'})
        },
        u'insuranceimapp.userinterfacetype': {
            'Meta': {'object_name': 'UserInterfaceType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'redirection_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'insuranceimapp.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'contacts_list': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'contacts_list'", 'default': 'None', 'to': u"orm['auth.User']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phonenumber': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '31'}),
            'phonenumber_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '7'}),
            'read_messages': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'read_messages'", 'default': 'None', 'to': u"orm['insuranceimapp.Message']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'unread_messages': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'unread_messages'", 'default': 'None', 'to': u"orm['insuranceimapp.Message']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'user_active': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '31'})
        }
    }

    complete_apps = ['insuranceimapp']