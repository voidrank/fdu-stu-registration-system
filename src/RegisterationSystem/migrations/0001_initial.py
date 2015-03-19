# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('grade', models.CharField(max_length=128)),
                ('stu_no', models.CharField(max_length=128, unique=True)),
                ('cellphone', models.CharField(max_length=128, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
