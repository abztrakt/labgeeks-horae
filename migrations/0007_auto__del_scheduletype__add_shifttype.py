# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ScheduleType'
        db.delete_table('labgeeks_schedule_scheduletype')

        # Removing M2M table for field allowed_groups on 'ScheduleType'
        db.delete_table('labgeeks_schedule_scheduletype_allowed_groups')

        # Adding model 'ShiftType'
        db.create_table('labgeeks_schedule_shifttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['labgeeks_chronos.Location'])),
            ('timeperiod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['labgeeks_schedule.TimePeriod'])),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('in_time', self.gf('django.db.models.fields.TimeField')()),
            ('out_time', self.gf('django.db.models.fields.TimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('labgeeks_schedule', ['ShiftType'])

        # Adding M2M table for field allowed_groups on 'ShiftType'
        db.create_table('labgeeks_schedule_shifttype_allowed_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('shifttype', models.ForeignKey(orm['labgeeks_schedule.shifttype'], null=False)),
            ('group', models.ForeignKey(orm['auth.group'], null=False))
        ))
        db.create_unique('labgeeks_schedule_shifttype_allowed_groups', ['shifttype_id', 'group_id'])

    def backwards(self, orm):
        # Adding model 'ScheduleType'
        db.create_table('labgeeks_schedule_scheduletype', (
            ('out_time', self.gf('django.db.models.fields.TimeField')()),
            ('in_time', self.gf('django.db.models.fields.TimeField')()),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['labgeeks_chronos.Location'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('timeperiod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['labgeeks_schedule.TimePeriod'])),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('labgeeks_schedule', ['ScheduleType'])

        # Adding M2M table for field allowed_groups on 'ScheduleType'
        db.create_table('labgeeks_schedule_scheduletype_allowed_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scheduletype', models.ForeignKey(orm['labgeeks_schedule.scheduletype'], null=False)),
            ('group', models.ForeignKey(orm['auth.group'], null=False))
        ))
        db.create_unique('labgeeks_schedule_scheduletype_allowed_groups', ['scheduletype_id', 'group_id'])

        # Deleting model 'ShiftType'
        db.delete_table('labgeeks_schedule_shifttype')

        # Removing M2M table for field allowed_groups on 'ShiftType'
        db.delete_table('labgeeks_schedule_shifttype_allowed_groups')

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
        'labgeeks_chronos.location': {
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
        'labgeeks_schedule.closedhour': {
            'Meta': {'object_name': 'ClosedHour'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_time': ('django.db.models.fields.TimeField', [], {}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_chronos.Location']"}),
            'out_time': ('django.db.models.fields.TimeField', [], {}),
            'timeperiod': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_schedule.TimePeriod']"})
        },
        'labgeeks_schedule.defaultshift': {
            'Meta': {'object_name': 'DefaultShift'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_time': ('django.db.models.fields.TimeField', [], {}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_chronos.Location']"}),
            'out_time': ('django.db.models.fields.TimeField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'timeperiod': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_schedule.TimePeriod']", 'null': 'True', 'blank': 'True'})
        },
        'labgeeks_schedule.shifttype': {
            'Meta': {'object_name': 'ShiftType'},
            'allowed_groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'day': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_time': ('django.db.models.fields.TimeField', [], {}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_chronos.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'out_time': ('django.db.models.fields.TimeField', [], {}),
            'timeperiod': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_schedule.TimePeriod']"})
        },
        'labgeeks_schedule.timeperiod': {
            'Meta': {'object_name': 'TimePeriod'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2012, 8, 14)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2012, 8, 14)'})
        },
        'labgeeks_schedule.workshift': {
            'Meta': {'object_name': 'WorkShift'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_chronos.Location']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'scheduled_in': ('django.db.models.fields.DateTimeField', [], {}),
            'scheduled_out': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['labgeeks_schedule']
