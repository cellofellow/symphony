# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 16:40
from __future__ import unicode_literals

from django.db import migrations

FORWARDS = [
    # Clear old triggers and table
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
    # Recreate everything.
    """
    CREATE VIRTUAL TABLE piece_search
    USING fts4 (id integer, body)
    """,
    """
    CREATE TRIGGER library_piece_search_insert
    AFTER INSERT ON library_piece
    FOR EACH ROW
    BEGIN
        INSERT INTO piece_search (id, body)
        VALUES (NEW.id, NEW.title || ' ' || NEW.subtitle || ' ' || NEW.comment);
    END
    """,
    """
    CREATE TRIGGER library_piece_search_update
    AFTER UPDATE ON library_piece
    FOR EACH ROW
    BEGIN
        UPDATE piece_search
        SET id = NEW.id,
            body = (
              SELECT
                  title || ' ' ||
                  subtitle || ' ' ||
                  comment || ' ' ||
                  GROUP_CONCAT(composer.given_names || ' ' || composer.surname) || ' ' ||
                  GROUP_CONCAT(arranger.given_names, arranger.surname)
              FROM library_piece AS piece
              LEFT OUTER JOIN library_piece_composer_artists AS pc
                           ON piece.id = pc.piece_id
              LEFT OUTER JOIN library_piece_arranger_artists AS pa
                           ON piece.id = pa.piece_id
                         JOIN library_artist AS composer
                           ON pc.artist_id = composer.id
                         JOIN library_artist AS arranger
                           ON pa.artist_id = arranger.id
              WHERE piece.id = OLD.id
            )
        WHERE id = OLD.id;
    END
    """,
    """
    CREATE TRIGGER library_piece_search_delete
    AFTER DELETE ON library_piece
    FOR EACH ROW
    BEGIN
        DELETE FROM piece_search
        WHERE id = OLD.id;
    END
    """,
    """
    CREATE TRIGGER library_piece_composer_artists_search_insert
    AFTER INSERT ON library_piece_composer_artists
    FOR EACH ROW
    BEGIN
        UPDATE piece_search
        SET body = (
              SELECT
                  title || ' ' ||
                  subtitle || ' ' ||
                  comment || ' ' ||
                  GROUP_CONCAT(composer.given_names || ' ' || composer.surname) || ' ' ||
                  GROUP_CONCAT(arranger.given_names, arranger.surname)
              FROM library_piece AS piece
              LEFT OUTER JOIN library_piece_composer_artists AS pc
                           ON piece.id = pc.piece_id
              LEFT OUTER JOIN library_piece_arranger_artists AS pa
                           ON piece.id = pa.piece_id
                         JOIN library_artist AS composer
                           ON pc.artist_id = composer.id
                         JOIN library_artist AS arranger
                           ON pa.artist_id = arranger.id
              WHERE piece.id = NEW.piece_id
            )
        WHERE id = NEW.piece_id;
    END
    """,
    """
    CREATE TRIGGER library_piece_composer_artists_search_update
    AFTER UPDATE ON library_piece_composer_artists
    FOR EACH ROW
    BEGIN
        UPDATE piece_search
        SET body = (
              SELECT
                  title || ' ' ||
                  subtitle || ' ' ||
                  comment || ' ' ||
                  GROUP_CONCAT(composer.given_names || ' ' || composer.surname) || ' ' ||
                  GROUP_CONCAT(arranger.given_names, arranger.surname)
              FROM library_piece AS piece
              LEFT OUTER JOIN library_piece_composer_artists AS pc
                           ON piece.id = pc.piece_id
              LEFT OUTER JOIN library_piece_arranger_artists AS pa
                           ON piece.id = pa.piece_id
                         JOIN library_artist AS composer
                           ON pc.artist_id = composer.id
                         JOIN library_artist AS arranger
                           ON pa.artist_id = arranger.id
              WHERE piece.id = NEW.piece_id
            )
        WHERE id = NEW.piece_id;
    END
    """,
    """
    CREATE TRIGGER library_piece_composer_artists_search_delete
    AFTER DELETE ON library_piece_composer_artists
    FOR EACH ROW
    BEGIN
        UPDATE piece_search
        SET body = (
              SELECT
                  title || ' ' ||
                  subtitle || ' ' ||
                  comment || ' ' ||
                  GROUP_CONCAT(composer.given_names || ' ' || composer.surname) || ' ' ||
                  GROUP_CONCAT(arranger.given_names, arranger.surname)
              FROM library_piece AS piece
              LEFT OUTER JOIN library_piece_composer_artists AS pc
                           ON piece.id = pc.piece_id
              LEFT OUTER JOIN library_piece_arranger_artists AS pa
                           ON piece.id = pa.piece_id
                         JOIN library_artist AS composer
                           ON pc.artist_id = composer.id
                         JOIN library_artist AS arranger
                           ON pa.artist_id = arranger.id
              WHERE piece.id = NEW.piece_id
            )
        WHERE id = NEW.piece_id;
    END
    """,
    """
    CREATE TRIGGER library_piece_arranger_artists_search_insert
    AFTER INSERT ON library_piece_arranger_artists
    FOR EACH ROW
    BEGIN
        UPDATE piece_search
        SET body = (
              SELECT
                  title || ' ' ||
                  subtitle || ' ' ||
                  comment || ' ' ||
                  GROUP_CONCAT(composer.given_names || ' ' || composer.surname) || ' ' ||
                  GROUP_CONCAT(arranger.given_names, arranger.surname)
              FROM library_piece AS piece
              LEFT OUTER JOIN library_piece_composer_artists AS pc
                           ON piece.id = pc.piece_id
              LEFT OUTER JOIN library_piece_arranger_artists AS pa
                           ON piece.id = pa.piece_id
                         JOIN library_artist AS composer
                           ON pc.artist_id = composer.id
                         JOIN library_artist AS arranger
                           ON pa.artist_id = arranger.id
              WHERE piece.id = NEW.piece_id
            )
        WHERE id = NEW.piece_id;
    END
    """,
    """
    CREATE TRIGGER library_piece_arranger_artists_search_update
    AFTER UPDATE ON library_piece_arranger_artists
    FOR EACH ROW
    BEGIN
        UPDATE piece_search
        SET body = (
              SELECT
                  title || ' ' ||
                  subtitle || ' ' ||
                  comment || ' ' ||
                  GROUP_CONCAT(composer.given_names || ' ' || composer.surname) || ' ' ||
                  GROUP_CONCAT(arranger.given_names, arranger.surname)
              FROM library_piece AS piece
              LEFT OUTER JOIN library_piece_composer_artists AS pc
                           ON piece.id = pc.piece_id
              LEFT OUTER JOIN library_piece_arranger_artists AS pa
                           ON piece.id = pa.piece_id
                         JOIN library_artist AS composer
                           ON pc.artist_id = composer.id
                         JOIN library_artist AS arranger
                           ON pa.artist_id = arranger.id
              WHERE piece.id = NEW.piece_id
            )
        WHERE id = NEW.piece_id;
    END
    """,
    """
    CREATE TRIGGER library_piece_arranger_artists_search_delete
    AFTER DELETE ON library_piece_arranger_artists
    FOR EACH ROW
    BEGIN
        UPDATE piece_search
        SET body = (
              SELECT
                  title || ' ' ||
                  subtitle || ' ' ||
                  comment || ' ' ||
                  GROUP_CONCAT(composer.given_names || ' ' || composer.surname) || ' ' ||
                  GROUP_CONCAT(arranger.given_names, arranger.surname)
              FROM library_piece AS piece
              LEFT OUTER JOIN library_piece_composer_artists AS pc
                           ON piece.id = pc.piece_id
              LEFT OUTER JOIN library_piece_arranger_artists AS pa
                           ON piece.id = pa.piece_id
                         JOIN library_artist AS composer
                           ON pc.artist_id = composer.id
                         JOIN library_artist AS arranger
                           ON pa.artist_id = arranger.id
              WHERE piece.id = NEW.piece_id
            )
        WHERE id = NEW.piece_id;
    END
    """,
    """
    INSERT INTO     piece_search
                    (id, body)
    SELECT          piece.id, piece.title || ' ' || piece.subtitle || ' ' || piece.comment || ' ' ||
                    GROUP_CONCAT(composer.given_names || ' ' || composer.surname) || ' ' ||
                    GROUP_CONCAT(arranger.given_names || ' ' || arranger.surname)
    FROM            library_piece AS piece
    LEFT OUTER JOIN library_piece_composer_artists AS pc ON piece.id = pc.piece_id
    LEFT OUTER JOIN library_piece_arranger_artists AS pa ON piece.id = pa.piece_id
    INNER JOIN      library_artist AS composer ON pc.artist_id = composer.id
    INNER JOIN      library_artist AS arranger ON pa.artist_id = arranger.id
    GROUP BY        piece.id
    """,
]

from ._0002_fts4 import FORWARDS as PREVIOUS_FORWARDS
REVERSE = [
    """DROP TRIGGER library_piece_arranger_artists_search_delete""",
    """DROP TRIGGER library_piece_arranger_artists_search_update""",
    """DROP TRIGGER library_piece_arranger_artists_search_insert""",
    """DROP TRIGGER library_piece_composer_artists_search_delete""",
    """DROP TRIGGER library_piece_composer_artists_search_update""",
    """DROP TRIGGER library_piece_composer_artists_search_insert""",
    """DROP TRIGGER library_piece_search_insert""",
    """DROP TRIGGER library_piece_search_update""",
    """DROP TRIGGER library_piece_search_delete""",
    """DROP TABLE piece_search""",
] + PREVIOUS_FORWARDS

class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_composer_arranger_to_artist'),
    ]

    operations = [
        migrations.RunSQL(FORWARDS, REVERSE),
    ]
