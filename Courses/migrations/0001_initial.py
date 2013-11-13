# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Deck'
        db.create_table(u'Courses_deck', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'Courses', ['Deck'])

        # Adding model 'Course'
        db.create_table(u'Courses_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'Courses', ['Course'])

        # Adding M2M table for field deck on 'Course'
        m2m_table_name = db.shorten_name(u'Courses_course_deck')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm[u'Courses.course'], null=False)),
            ('deck', models.ForeignKey(orm[u'Courses.deck'], null=False))
        ))
        db.create_unique(m2m_table_name, ['course_id', 'deck_id'])

        # Adding model 'Card'
        db.create_table(u'Courses_card', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idea', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('gist', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'Courses', ['Card'])

        # Adding M2M table for field deck on 'Card'
        m2m_table_name = db.shorten_name(u'Courses_card_deck')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('card', models.ForeignKey(orm[u'Courses.card'], null=False)),
            ('deck', models.ForeignKey(orm[u'Courses.deck'], null=False))
        ))
        db.create_unique(m2m_table_name, ['card_id', 'deck_id'])


    def backwards(self, orm):
        # Deleting model 'Deck'
        db.delete_table(u'Courses_deck')

        # Deleting model 'Course'
        db.delete_table(u'Courses_course')

        # Removing M2M table for field deck on 'Course'
        db.delete_table(db.shorten_name(u'Courses_course_deck'))

        # Deleting model 'Card'
        db.delete_table(u'Courses_card')

        # Removing M2M table for field deck on 'Card'
        db.delete_table(db.shorten_name(u'Courses_card_deck'))


    models = {
        u'Courses.card': {
            'Meta': {'object_name': 'Card'},
            'deck': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Courses.Deck']", 'symmetrical': 'False'}),
            'gist': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'Courses.course': {
            'Meta': {'object_name': 'Course'},
            'deck': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Courses.Deck']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'Courses.deck': {
            'Meta': {'object_name': 'Deck'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['Courses']