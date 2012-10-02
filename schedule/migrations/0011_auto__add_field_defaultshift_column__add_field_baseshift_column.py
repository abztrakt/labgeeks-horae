# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):

        # Adding field 'DefaultShift.column'
        db.add_column('schedule_defaultshift', 'column', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Adding field 'BaseShift.column'
        db.add_column('schedule_baseshift', 'column', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

    def backwards(self, orm):

        # Deleting field 'DefaultShift.column'
        db.delete_column('schedule_defaultshift', 'column')

        # Deleting field 'BaseShift.column'
        db.delete_column('schedule_baseshift', 'column')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'chronos.location': {
            'Meta': {'object_name': 'Location'},
            'active_users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'schedule.baseshift': {
            'Meta': {'object_name': 'BaseShift'},
            'column': ('django.db.models.fields.IntegerField', [], {}),
            'day': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_time': ('django.db.models.fields.TimeField', [], {}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chronos.Location']"}),
            'out_time': ('django.db.models.fields.TimeField', [], {}),
            'shift_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.ShiftType']", 'null': 'True', 'blank': 'True'}),
            'timeperiod': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.TimePeriod']", 'null': 'True', 'blank': 'True'})
        },
        'schedule.closedhour': {
            'Meta': {'object_name': 'ClosedHour'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_time': ('django.db.models.fields.TimeField', [], {}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chronos.Location']"}),
            'out_time': ('django.db.models.fields.TimeField', [], {}),
            'timeperiod': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.TimePeriod']"})
        },
        'schedule.defaultshift': {
            'Meta': {'object_name': 'DefaultShift'},
            'column': ('django.db.models.fields.IntegerField', [], {}),
            'day': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_time': ('django.db.models.fields.TimeField', [], {}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chronos.Location']"}),
            'out_time': ('django.db.models.fields.TimeField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'timeperiod': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.TimePeriod']", 'null': 'True', 'blank': 'True'})
        },
        'schedule.shifttype': {
            'Meta': {'object_name': 'ShiftType'},
            'allowed_groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'schedule.timeperiod': {
            'Meta': {'object_name': 'TimePeriod'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2012, 9, 17)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2012, 9, 17)'})
        },
        'schedule.workshift': {
            'Meta': {'object_name': 'WorkShift'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chronos.Location']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'scheduled_in': ('django.db.models.fields.DateTimeField', [], {}),
            'scheduled_out': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['schedule']
