# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import livefield.fields
import animals.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('featured', models.BooleanField(default=False)),
                ('live', livefield.fields.LiveField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('birth_date', models.DateField(verbose_name='date of birth')),
                ('microchip_id', models.CharField(max_length=255, blank=True)),
                ('about', models.TextField()),
                ('private', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'animals',
                'get_latest_by': 'created',
                'ordering': ('-created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('featured', models.BooleanField(default=False)),
                ('live', livefield.fields.LiveField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('featured', models.BooleanField(default=False)),
                ('live', livefield.fields.LiveField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('featured', models.BooleanField(default=False)),
                ('live', livefield.fields.LiveField(default=True)),
                ('interval', models.CharField(choices=[('Hour', 'Hour'), ('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month')], max_length=5, default='Day')),
                ('alt_food', models.CharField(max_length=255, blank=True)),
                ('food_amount', models.DecimalField(max_digits=3, decimal_places=2, verbose_name='amount')),
                ('food_measurement', models.CharField(choices=[('Each', 'Each'), ('Tspn', 'Teaspoon'), ('Tblsp', 'Tablespoon'), ('Cup', 'Cup'), ('Ml', 'Milliliter'), ('G', 'Gram'), ('MG', 'Milligram')], max_length=9, default='Each', verbose_name='measurement')),
                ('occurrence', animals.models.IntegerRangeField()),
                ('note', models.TextField(blank=True)),
                ('animal', models.ForeignKey(to='animals.Animal')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('featured', models.BooleanField(default=False)),
                ('live', livefield.fields.LiveField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('upc', models.CharField(max_length=12)),
                ('brand', models.ForeignKey(to='animals.Brand')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('featured', models.BooleanField(default=False)),
                ('live', livefield.fields.LiveField(default=True)),
                ('street', models.CharField(max_length=200)),
                ('block', models.CharField(max_length=200, blank=True)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=175)),
                ('country', models.CharField(max_length=60)),
                ('postal_code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='feeding',
            name='food',
            field=models.ForeignKey(to='animals.Food'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='animal',
            name='breed',
            field=models.ForeignKey(to='animals.Breed'),
            preserve_default=True,
        ),
    ]
