# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-12 16:41
from __future__ import unicode_literals

import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('resolved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(blank=True, max_length=255)),
                ('course', models.CharField(blank=True, max_length=255)),
                ('year_of_graduation', models.IntegerField(choices=[(2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027)], default=2018, verbose_name='year')),
                ('bio', models.TextField(blank=True)),
                ('email', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('linkedIn', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(default='default/Default_avatar.jpg', upload_to='user/avatar/')),
                ('user_badge_text', models.CharField(max_length=255, null=True)),
                ('user_badge_icon', models.CharField(max_length=255, null=True)),
                ('club', models.ManyToManyField(to='home.Club')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='reported_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_by', to='log.UserProfile'),
        ),
        migrations.AddField(
            model_name='report',
            name='reported_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_user', to='log.UserProfile'),
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received', to='log.UserProfile'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent', to='log.UserProfile'),
        ),
    ]
