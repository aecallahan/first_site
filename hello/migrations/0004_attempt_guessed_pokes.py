# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20151014_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='guessed_pokes',
            field=models.CharField(default=b'[]', max_length=2000),
        ),
    ]
