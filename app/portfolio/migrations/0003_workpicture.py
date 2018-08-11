# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20151018_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('src', models.ImageField(upload_to='')),
                ('work', models.ForeignKey(to='portfolio.Work', on_delete=models.CASCADE)),
            ],
        ),
    ]
