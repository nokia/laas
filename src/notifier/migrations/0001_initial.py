# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-14 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import fernet_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0002_auto_20170505_0815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=240)),
                ('content', fernet_fields.fields.EncryptedTextField()),
                ('sender', models.CharField(default='unknown', max_length=240)),
                ('message_type', models.CharField(choices=[('email', 'Email'), ('webnotification', 'Web Notification')], default='email', max_length=240)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.UserProfile')),
            ],
        ),
    ]
