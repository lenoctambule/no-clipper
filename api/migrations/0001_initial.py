# Generated by Django 4.1.7 on 2023-03-08 16:06

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('ip', models.GenericIPAddressField(primary_key=True, serialize=False, unique=True)),
                ('org', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('isp', models.CharField(max_length=100)),
                ('discovered_on', models.DateTimeField(auto_now_add=True)),
                ('lastscan_on', models.DateTimeField(auto_now_add=True)),
                ('open_ports', models.CharField(max_length=1000, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=100)),
                ('banner', models.TextField()),
                ('port', models.IntegerField()),
            ],
        ),
    ]
