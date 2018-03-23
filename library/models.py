from enum import Enum

from django.db import models
from django.urls import reverse


class Artist(models.Model):
    surname = models.CharField('Surname', max_length=100)
    given_names = models.CharField('Given Names', max_length=1000)

    def __str__(self):
        return '{self.surname}, {self.given_names}'.format(self=self)

    def get_absolute_url(self):
        return reverse('library.views.composer_list', args=[str(self.id)])

    class Meta:
        ordering = ('surname', 'given_names')
        unique_together = ('surname', 'given_names')


class Score(Enum):
    NO_SCORE = 'No Score'
    CONDENSED = 'Condensed'
    PIANO = 'Piano'
    FULL = 'Full'


class Difficulty(Enum):
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'
    PROFESSIONAL = 'Professional'


class Piece(models.Model):
    id = models.IntegerField('Catalog ID Number', primary_key=True)
    location = models.ForeignKey('Location', models.PROTECT)
    title = models.CharField('Title', max_length=256)
    subtitle = models.CharField('Subtitle (Optional)', max_length=128,
                                blank=True)
    composer_artists = models.ManyToManyField('Artist',
                                              related_name='pieces_composed',
                                              blank=True)
    arranger_artists = models.ManyToManyField('Artist',
                                              related_name='pieces_arranged',
                                              blank=True)
    score_type = models.CharField('Score Type', max_length=12,
                                  choices=[(s.name, s.value)
                                           for s in Score],
                                  blank=True, null=True)
    difficulty = models.CharField('Difficulty Level', max_length=12,
                                  choices=[(s.name, s.value)
                                           for s in Difficulty],
                                  blank=True, null=True)
    comment = models.TextField('Comment', max_length=1024, blank=True)

    def __str__(self):
        return "%d: %s" % (self.id, self.title)

    def get_absolute_url(self):
        return reverse('piece_detail', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('admin:library_piece_change', args=[self.id])

    class Meta:
        ordering = ['title']

    @classmethod
    def search(cls, term: str):
        return Piece.objects.raw(
            """
            SELECT piece.*
            FROM piece_search
            JOIN library_piece AS piece
              ON piece_search.id = piece.id
            WHERE piece_search.body MATCH %s
            """,
            [term])


class Location(models.Model):
    identifier = models.CharField(max_length=100)
    parent = models.ForeignKey("Location", models.PROTECT,
                               null=True, blank=True,
                               related_name='children')

    def __str__(self):
        if self.parent:
            return '{} >> {}'.format(self.parent, self.identifier)
        return self.identifier

    def get_absolute_url(self):
        return reverse('location_detail', args=[self.pk])

    class Meta:
        unique_together = (
            ('identifier', 'parent'),
        )


class Orchestra(models.Model):
    shortname = models.CharField('Short Name', max_length=5, unique=True)
    name = models.CharField('Full Name', max_length=64)

    def __str__(self):
        return self.shortname

    class Meta:
        ordering = ['shortname']


class Performance(models.Model):
    place = models.TextField('Place', max_length=1024)
    date = models.DateField('Date')
    orchestra = models.ManyToManyField('Orchestra')
    piece = models.ManyToManyField('Piece')

    def __str__(self):
        return '{}: {}'.format(self.date, self.place)

    def get_absolute_url(self):
        return reverse('performance_detail', kwargs={'object_id': self.id})

    def get_edit_url(self):
        return reverse('admin', args=['library/performance/%d/' % self.id])

    class Meta:
        ordering = ['date']
