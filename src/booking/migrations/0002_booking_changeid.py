# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-13 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opsys',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='opsys',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='booking.Opsys'),
        ),
        migrations.AddField(
            model_name='booking',
            name='changeid',
            field=models.TextField(default='no change ID'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='changeid',
            field=models.TextField(blank=True, default='no change ID', null=True),
        ),
    ]