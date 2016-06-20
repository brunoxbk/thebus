# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-19 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_line', models.CharField(max_length=50, verbose_name='Code')),
                ('denomination', models.CharField(max_length=50, verbose_name='Name')),
                ('origin', models.CharField(blank=True, max_length=50, null=True, verbose_name='Origin')),
                ('line_return', models.CharField(blank=True, max_length=50, null=True, verbose_name='Return')),
                ('circle', models.BooleanField(default=False, verbose_name='Circle')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('changed_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Changed at')),
            ],
            options={
                'ordering': ['-created_at'],
                'get_latest_by': '-created_at',
            },
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_stop', models.CharField(max_length=50, verbose_name='Code')),
                ('denomination', models.CharField(max_length=50, verbose_name='Denomination')),
                ('lat', models.CharField(blank=True, max_length=50, null=True, verbose_name='Latitude')),
                ('lon', models.CharField(blank=True, max_length=50, null=True, verbose_name='Longitude')),
                ('address', models.CharField(blank=True, max_length=140, null=True, verbose_name='Address')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('changed_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Changed at')),
            ],
            options={
                'ordering': ['-created_at'],
                'get_latest_by': '-created_at',
            },
        ),
    ]
