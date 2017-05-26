# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arranger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=32, verbose_name='Last Name')),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Cabinet ID Number')),
            ],
            options={
                'ordering': ['group', 'number'],
            },
        ),
        migrations.CreateModel(
            name='CabinetGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=5, unique=True, verbose_name='Short Name')),
                ('description', models.CharField(max_length=140, verbose_name='Description')),
            ],
            options={
                'ordering': ['shortname'],
            },
        ),
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=32, verbose_name='Last Name')),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Drawer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(verbose_name='Drawer Number')),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Cabinet')),
            ],
            options={
                'ordering': ['cabinet', 'number'],
            },
        ),
        migrations.CreateModel(
            name='Orchestra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=5, unique=True, verbose_name='Short Name')),
                ('name', models.CharField(max_length=64, verbose_name='Full Name')),
            ],
            options={
                'ordering': ['shortname'],
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.TextField(max_length=1024, verbose_name='Place')),
                ('date', models.DateField(verbose_name='Date')),
                ('orchestra', models.ManyToManyField(to='library.Orchestra')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Catalog ID Number')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('subtitle', models.CharField(blank=True, max_length=128, verbose_name='Subtitle (Optional)')),
                ('difficulty', models.SmallIntegerField(blank=True, choices=[('0', 'Unknown'), ('1', 'Beginner'), ('2', 'Intermediate'), ('3', 'Advanced'), ('4', 'Insane')], null=True, verbose_name='Difficulty Level')),
                ('comment', models.TextField(blank=True, max_length=1024, verbose_name='Comment')),
                ('arranger', models.ManyToManyField(blank=True, null=True, to='library.Arranger')),
                ('composer', models.ManyToManyField(to='library.Composer')),
                ('drawer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Drawer')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ScoreType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='Short Name')),
                ('description', models.CharField(max_length=140, verbose_name='Description')),
            ],
        ),
        migrations.AddField(
            model_name='piece',
            name='score',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.ScoreType'),
        ),
        migrations.AddField(
            model_name='performance',
            name='piece',
            field=models.ManyToManyField(to='library.Piece'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.CabinetGroup'),
        ),
    ]
