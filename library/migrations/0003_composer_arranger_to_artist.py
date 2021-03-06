# Generated by Django 2.0.2 on 2018-02-27 01:35

from django.db import migrations, models
from itertools import chain


def forwards(apps, schema_editor):
    Artist = apps.get_model('library', 'Artist')
    Composer = apps.get_model('library', 'Composer')
    Arranger = apps.get_model('library', 'Arranger')

    names = {}
    for old in chain(Composer.objects.all(), Arranger.objects.all()):
        name = (old.first_name, old.last_name)
        lst = names.get(name, [])
        lst.append(old)
        names[name] = lst

    for name, lst in names.items():
        artist = Artist.objects.create(surname=name[1], given_names=name[0])
        for old in lst:
            for piece in old.piece_set.all():
                rel = getattr(piece, old._meta.model_name + '_artists')
                rel.add(artist)


def reverse(apps, schema_editor):
    Artist = apps.get_model('library', 'Artist')
    Composer = apps.get_model('library', 'Composer')
    Arranger = apps.get_model('library', 'Arranger')

    for artist in Artist.objects.all():
        composer = None
        if artist.pieces_composed.exists():
            composer, _ = Composer.objects.get_or_create(
                last_name=artist.surname, first_name=artist.given_names)
        for piece in artist.pieces_composed.all():
            piece.composer.add(composer)

        arranger = None
        if artist.pieces_arranged.exists():
            arranger, _ = Arranger.objects.get_or_create(
                last_name=artist.surname, first_name=artist.given_names)
        for piece in artist.pieces_arranged.all():
            piece.arranger.add(arranger)


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_fts4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100, verbose_name='Surname')),
                ('given_names', models.CharField(max_length=1000, verbose_name='Given Names')),
            ],
            options={
                'ordering': ('surname', 'given_names'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='artist',
            unique_together={('surname', 'given_names')},
        ),
        migrations.AddField(
            model_name='piece',
            name='composer_artists',
            field=models.ManyToManyField(related_name='pieces_composed', to='library.Artist'),
        ),
        migrations.AddField(
            model_name='piece',
            name='arranger_artists',
            field=models.ManyToManyField(related_name='pieces_arranged', to='library.Artist'),
        ),
        migrations.RunPython(forwards, reverse, elidable=True),
    ]
