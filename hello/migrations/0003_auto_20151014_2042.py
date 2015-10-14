# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20151013_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='last_guess',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='attempt',
            name='last_poke_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='attempt',
            name='player_name',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
