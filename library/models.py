from django.db import models
from django.urls import reverse

class Composer(models.Model):
    first_name = models.CharField('First Name', max_length=32)
    last_name = models.CharField('Last Name', max_length=32)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('library.views.composer_list', [str(self.id)])

    def get_edit_url(self):
        return reverse('admin', args=['library/composer/%d/' % self.id])

    class Meta:
        ordering = ['last_name']

class Arranger(models.Model):
    first_name = models.CharField('First Name', max_length=32)
    last_name = models.CharField('Last Name', max_length=32)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('library.views.arranger_list', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('admin', args=['library/arranger/%d/' % self.id])

    class Meta:
        ordering = ['last_name']

class Piece(models.Model):
    DIFFICULTY_CHOICES = (
        ('0', 'Unknown'),
        ('1', 'Beginner'),
        ('2', 'Intermediate'),
        ('3', 'Advanced'),
        ('4', 'Insane'),
    )

    id = models.IntegerField('Catalog ID Number', primary_key=True)
    drawer = models.ForeignKey('Drawer')
    title = models.CharField('Title', max_length=256)
    subtitle = models.CharField('Subtitle (Optional)', max_length=128,
                                blank=True)
    composer = models.ManyToManyField('Composer')
    arranger = models.ManyToManyField('Arranger')
    score = models.ForeignKey('ScoreType', blank=True, null=True)
    difficulty = models.SmallIntegerField('Difficulty Level',
                                          choices=DIFFICULTY_CHOICES,
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
              ON piece_search.rowid = piece.id
            WHERE piece_search.body MATCH %s
            """,
            [term])

class ScoreType(models.Model):
    name = models.CharField('Short Name', max_length=16)
    description = models.CharField('Description', max_length=140)

    def __str__(self):
        return "%s" % self.name

class CabinetGroup(models.Model):
    shortname = models.CharField('Short Name', max_length=5, unique=True)
    description = models.CharField('Description', max_length=140)

    def __str__(self):
        return "%s" % self.shortname

    def get_absolute_url(self):
        return reverse('library.views.group_list',
                       kwargs={'group_name': self.shortname})

    def get_edit_url(self):
        return reverse('admin', args=['library/cabinetgroup/%d/' % self.id])

    class Meta:
        ordering = ['shortname']

class Cabinet(models.Model):
    number = models.IntegerField('Cabinet ID Number')
    group = models.ForeignKey('CabinetGroup')

    def __str__(self):
        return "%s >> %s" % (self.group, self.number)

    def __int__(self):
        return self.number

    def get_absolute_url(self):
        return reverse('library.views.cabinet_list', kwargs={
            'group_name': self.group.shortname,
            'cabinet_id': str(int(self)),
        })

    def get_edit_url(self):
        return reverse('admin', args=['library/cabinet/%d/' % self.id])

    class Meta:
        ordering = ['group', 'number']

class Drawer(models.Model):
    cabinet = models.ForeignKey('Cabinet')
    number = models.SmallIntegerField('Drawer Number')

    def __str__(self):
        return "%s >> %s" % (self.cabinet, self.number)

    def __int__(self):
        return self.number

    def get_absolute_url(self):
        return reverse('library.views.drawer_list', kwargs={
            'group_name': self.cabinet.group,
            'cabinet_id': str(int(self.cabinet)),
            'drawer_id': str(int(self))
        })

    def get_edit_url(self):
        return reverse('admin', args=['library/drawer/%d/' % self.id])

    class Meta:
        ordering = ['cabinet', 'number']

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
        return self.date + ': ' + self.place

    def get_absolute_url(self):
        return reverse('performance_detail', kwargs={'object_id': self.id})

    def get_edit_url(self):
        return reverse('admin', args=['library/performance/%d/' % self.id])

    class Meta:
        ordering = ['date']
