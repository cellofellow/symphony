# Generated by Django 2.0.2 on 2018-02-28 00:28

import re

from django.db import migrations, models
import django.db.models.deletion


def forwards(apps, schema_editor):
    CabinetGroup = apps.get_model('library', 'CabinetGroup')
    Location = apps.get_model('library', 'Location')

    for cbntgrp in CabinetGroup.objects.all():
        root = Location.objects.create(
            identifier='{} ({})'.format(cbntgrp.description,
                                        cbntgrp.shortname))
        for cbnt in cbntgrp.cabinet_set.all():
            branch = Location.objects.create(
                identifier=str(cbnt.number), parent=root)
            for drawer in cbnt.drawer_set.all():
                leaf = Location.objects.create(
                    identifier=str(drawer.number), parent=branch)
                drawer.piece_set.all().update(location=leaf)


def reverse(apps, schema_editor):
    Location = apps.get_model('library', 'Location')
    CabinetGroup = apps.get_model('library', 'CabinetGroup')
    Cabinet = apps.get_model('library', 'Cabinet')
    Drawer = apps.get_model('library', 'Drawer')

    root_pattern = re.compile(r'([\w\s]+) \((\w{0,5})\)')

    for root in Location.objects.filter(parent__isnull=True):
        match = root_pattern.match(root.identifier)
        if match:
            description, shortname = match.groups()
        else:
            shortname = str(match.id)
            description = root.identifier
        cbntgrp, _ = CabinetGroup.objects.get_or_create(
            shortname=shortname,
            description=description)
        for branch in root.children.all():
            cabinet, _ = Cabinet.objects.get_or_create(
                number=int(branch.identifier), group=cbntgrp)
            for leaf in branch.children.all():
                drawer, _ = Drawer.objects.get_or_create(
                    number=int(leaf.identifier),
                    cabinet=cabinet)
                leaf.piece_set.all().update(drawer=drawer)


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20180228_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.Location', null=True, blank=True, related_name='children')),
            ],
        ),
        migrations.AddField(
            model_name='piece',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='library.Location'),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('identifier', 'parent')},
        ),
        migrations.RunPython(forwards, reverse, elidable=True),
    ]
