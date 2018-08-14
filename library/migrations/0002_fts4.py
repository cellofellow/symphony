# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 16:40
from __future__ import unicode_literals

from django.db import migrations

from .._0002_sql import FORWARDS

REVERSE = [
    """DROP TRIGGER library_piece_arranger_search_delete""",
    """DROP TRIGGER library_piece_arranger_search_update""",
    """DROP TRIGGER library_piece_arranger_search_insert""",
    """DROP TRIGGER library_piece_composer_search_delete""",
    """DROP TRIGGER library_piece_composer_search_update""",
    """DROP TRIGGER library_piece_composer_search_insert""",
    """DROP TRIGGER library_piece_search_insert""",
    """DROP TRIGGER library_piece_search_update""",
    """DROP TRIGGER library_piece_search_delete""",
    """DROP TABLE piece_search""",
]

class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(FORWARDS, REVERSE),
    ]
