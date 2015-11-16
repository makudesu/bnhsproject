# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='email address')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('middle_name', models.CharField(max_length=30, verbose_name='middle name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('sex', models.CharField(max_length=1, verbose_name='sex', choices=[(b'', b''), (b'M', b'Male'), (b'F', b'Female')])),
                ('date_of_birth', models.DateField(null=True, verbose_name='date of birth')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into admin', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'permissions': (('view_task', 'View task'),),
            },
        ),
    ]
