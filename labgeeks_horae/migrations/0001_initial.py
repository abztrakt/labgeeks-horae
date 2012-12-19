# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TimePeriod'
        db.create_table('labgeeks_horae_timeperiod', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(default=datetime.date(2012, 11, 16))),
            ('end_date', self.gf('django.db.models.fields.DateField')(default=datetime.date(2012, 11, 16))),
        ))
        db.send_create_signal('labgeeks_horae', ['TimePeriod'])

        # Adding model 'WorkShift'
        db.create_table('labgeeks_horae_workshift', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('scheduled_in', self.gf('django.db.models.fields.DateTimeField')()),
            ('scheduled_out', self.gf('django.db.models.fields.DateTimeField')()),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['labgeeks_chronos.Location'])),
        ))
        db.send_create_signal('labgeeks_horae', ['WorkShift'])

        # Adding model 'ShiftType'
        db.create_table('labgeeks_horae_shifttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('labgeeks_horae', ['ShiftType'])

        # Adding M2M table for field allowed_groups on 'ShiftType'
        db.create_table('labgeeks_horae_shifttype_allowed_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('shifttype', models.ForeignKey(orm['labgeeks_horae.shifttype'], null=False)),
            ('group', models.ForeignKey(orm['auth.group'], null=False))
        ))
        db.create_unique('labgeeks_horae_shifttype_allowed_groups', ['shifttype_id', 'group_id'])

        # Adding model 'DefaultShift'
        db.create_table('labgeeks_horae_defaultshift', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('in_time', self.gf('django.db.models.fields.TimeField')()),
            ('out_time', self.gf('django.db.models.fields.TimeField')()),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['labgeeks_chronos.Location'])),
            ('timeperiod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['labgeeks_horae.TimePeriod'], null=True, blank=True)),
        ))
        db.send_create_signal('labgeeks_horae', ['DefaultShift'])

        # Adding model 'BaseShift'
        db.create_table('labgeeks_horae_baseshift', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('in_time', self.gf('django.db.models.fields.TimeField')()),
            ('out_time', self.gf('django.db.models.fields.TimeField')()),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['labgeeks_chronos.Location'])),
            ('timeperiod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['labgeeks_horae.TimePeriod'], null=True, blank=True)),
            ('shift_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['labgeeks_horae.ShiftType'], null=True, blank=True)),
        ))
        db.send_create_signal('labgeeks_horae', ['BaseShift'])

        # Adding model 'ClosedHour'
        db.create_table('labgeeks_horae_closedhour', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('in_time', self.gf('django.db.models.fields.TimeField')()),
            ('out_time', self.gf('django.db.models.fields.TimeField')()),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['labgeeks_chronos.Location'])),
            ('timeperiod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['labgeeks_horae.TimePeriod'])),
        ))
        db.send_create_signal('labgeeks_horae', ['ClosedHour'])


    def backwards(self, orm):
        
        # Deleting model 'TimePeriod'
        db.delete_table('labgeeks_horae_timeperiod')

        # Deleting model 'WorkShift'
        db.delete_table('labgeeks_horae_workshift')

        # Deleting model 'ShiftType'
        db.delete_table('labgeeks_horae_shifttype')

        # Removing M2M table for field allowed_groups on 'ShiftType'
        db.delete_table('labgeeks_horae_shifttype_allowed_groups')

        # Deleting model 'DefaultShift'
        db.delete_table('labgeeks_horae_defaultshift')

        # Deleting model 'BaseShift'
        db.delete_table('labgeeks_horae_baseshift')

        # Deleting model 'ClosedHour'
        db.delete_table('labgeeks_horae_closedhour')


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 11, 16, 13, 15, 25, 993001)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 11, 16, 13, 15, 25, 992943)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'labgeeks_chronos.location': {
            'Meta': {'object_name': 'Location'},
            'active_users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'labgeeks_horae.baseshift': {
            'Meta': {'object_name': 'BaseShift'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_time': ('django.db.models.fields.TimeField', [], {}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_chronos.Location']"}),
            'out_time': ('django.db.models.fields.TimeField', [], {}),
            'shift_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_horae.ShiftType']", 'null': 'True', 'blank': 'True'}),
            'timeperiod': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_horae.TimePeriod']", 'null': 'True', 'blank': 'True'})
        },
        'labgeeks_horae.closedhour': {
            'Meta': {'object_name': 'ClosedHour'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_time': ('django.db.models.fields.TimeField', [], {}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_chronos.Location']"}),
            'out_time': ('django.db.models.fields.TimeField', [], {}),
            'timeperiod': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_horae.TimePeriod']"})
        },
        'labgeeks_horae.defaultshift': {
            'Meta': {'object_name': 'DefaultShift'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_time': ('django.db.models.fields.TimeField', [], {}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_chronos.Location']"}),
            'out_time': ('django.db.models.fields.TimeField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'timeperiod': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_horae.TimePeriod']", 'null': 'True', 'blank': 'True'})
        },
        'labgeeks_horae.shifttype': {
            'Meta': {'object_name': 'ShiftType'},
            'allowed_groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'labgeeks_horae.timeperiod': {
            'Meta': {'object_name': 'TimePeriod'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2012, 11, 16)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2012, 11, 16)'})
        },
        'labgeeks_horae.workshift': {
            'Meta': {'object_name': 'WorkShift'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_chronos.Location']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'scheduled_in': ('django.db.models.fields.DateTimeField', [], {}),
            'scheduled_out': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['labgeeks_horae']
