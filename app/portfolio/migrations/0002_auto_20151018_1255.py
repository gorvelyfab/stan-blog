# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='client_name',
            field=models.CharField(verbose_name='client', max_length=255, default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='client_url',
            field=models.URLField(default=False),
            preserve_default=False,
        ),
    ]
