# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='profile_img',
            field=models.ImageField(upload_to='pic_folder/', blank=True, default='pic_folder/None/no-img.jpg'),
            preserve_default=True,
        ),
    ]
