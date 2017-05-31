# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 16:40
from __future__ import unicode_literals

from django.db import migrations

FORWARDS = [
    """
    CREATE VIRTUAL TABLE piece_search
    USING fts4 (body)
    """,
    """
    CREATE TRIGGER library_piece_search_insert
    AFTER INSERT ON library_piece
    FOR EACH ROW
    BEGIN
        INSERT INTO piece_search (docid, body)
        VALUES (NEW.id, NEW.title || ' ' || NEW.subtitle || ' ' || NEW.comment);
    END
    """,
    """
    CREATE TRIGGER library_piece_search_update
    AFTER UPDATE ON library_piece
    FOR EACH ROW
    BEGIN
        UPDATE piece_search
        SET docid = NEW.id,
            body = (
              SELECT
                  title || ' ' ||
                  subtitle || ' ' ||
                  comment || ' ' ||
                  GROUP_CONCAT(composer.first_name || ' ' || composer.last_name) || ' ' ||
                  GROUP_CONCAT(arranger.first_name, arranger_last_name)
              FROM library_piece AS piece
              LEFT OUTER JOIN library_piece_composer AS pc
                           ON piece.id = pc.piece_id
              LEFT OUTER JOIN library_piece_arranger AS pa
                           ON piece.id = pa.piece_id
                         JOIN library_composer AS composer
                           ON pc.composer_id = composer.id
                         JOIN library_arranger AS arranger
                           ON pa.arranger_id = arranger.id
              WHERE piece.id = OLD.id
            )
        WHERE docid = OLD.id;
    END
    """,
    """
    CREATE TRIGGER library_piece_search_delete
    AFTER DELETE ON library_piece
    FOR EACH ROW
    BEGIN
        DELETE FROM piece_search
        WHERE docid = OLD.id;
    END
    """,
    """
    CREATE TRIGGER library_piece_composer_search_insert
    AFTER INSERT ON library_piece_composer
    FOR EACH ROW
    BEGIN
        UPDATE piece_search
        SET body = (
              SELECT
                  title || ' ' ||
                  subtitle || ' ' ||
                  comment || ' ' ||
                  GROUP_CONCAT(composer.first_name || ' ' || composer.last_name) || ' ' ||
                  GROUP_CONCAT(arranger.first_name, arranger_last_name)
              FROM library_piece AS piece
              LEFT OUTER JOIN library_piece_composer AS pc
                           ON piece.id = pc.piece_id
              LEFT OUTER JOIN library_piece_arranger AS pa
                           ON piece.id = pa.piece_id
                         JOIN library_composer AS composer
                           ON pc.composer_id = composer.id
                         JOIN library_arranger AS arranger
                           ON pa.arranger_id = arranger.id
              WHERE piece.id = NEW.piece_id
            )
        WHERE docid = NEW.piece_id;
    END
    """,
    """
    CREATE TRIGGER library_piece_composer_search_update
    AFTER UPDATE ON library_piece_composer
    FOR EACH ROW
    BEGIN
        UPDATE piece_search
        SET body = (
              SELECT
                  title || ' ' ||
                  subtitle || ' ' ||
                  comment || ' ' ||
                  GROUP_CONCAT(composer.first_name || ' ' || composer.last_name) || ' ' ||
                  GROUP_CONCAT(arranger.first_name, arranger_last_name)
              FROM library_piece AS piece
              LEFT OUTER JOIN library_piece_composer AS pc
                           ON piece.id = pc.piece_id
              LEFT OUTER JOIN library_piece_arranger AS pa
                           ON piece.id = pa.piece_id
                         JOIN library_composer AS composer
                           ON pc.composer_id = composer.id
                         JOIN library_arranger AS arranger
                           ON pa.arranger_id = arranger.id
              WHERE piece.id = NEW.piece_id
            )
        WHERE docid = NEW.piece_id;
    END
    """,
    """
    CREATE TRIGGER library_piece_composer_search_delete
    AFTER DELETE ON library_piece_composer
    FOR EACH ROW
    BEGIN
        UPDATE piece_search
        SET body = (
              SELECT
                  title || ' ' ||
                  subtitle || ' ' ||
                  comment || ' ' ||
                  GROUP_CONCAT(composer.first_name || ' ' || composer.last_name) || ' ' ||
                  GROUP_CONCAT(arranger.first_name, arranger_last_name)
              FROM library_piece AS piece
              LEFT OUTER JOIN library_piece_composer AS pc
                           ON piece.id = pc.piece_id
              LEFT OUTER JOIN library_piece_arranger AS pa
                           ON piece.id = pa.piece_id
                         JOIN library_composer AS composer
                           ON pc.composer_id = composer.id
                         JOIN library_arranger AS arranger
                           ON pa.arranger_id = arranger.id
              WHERE piece.id = NEW.piece_id
            )
        WHERE docid = NEW.piece_id;
    END
    """,
    """
    CREATE TRIGGER library_piece_arranger_search_insert
    AFTER INSERT ON library_piece_arranger
    FOR EACH ROW
    BEGIN
        UPDATE piece_search
        SET body = (
              SELECT
                  title || ' ' ||
                  subtitle || ' ' ||
                  comment || ' ' ||
                  GROUP_CONCAT(composer.first_name || ' ' || composer.last_name) || ' ' ||
                  GROUP_CONCAT(arranger.first_name, arranger_last_name)
              FROM library_piece AS piece
              LEFT OUTER JOIN library_piece_composer AS pc
                           ON piece.id = pc.piece_id
              LEFT OUTER JOIN library_piece_arranger AS pa
                           ON piece.id = pa.piece_id
                         JOIN library_composer AS composer
                           ON pc.composer_id = composer.id
                         JOIN library_arranger AS arranger
                           ON pa.arranger_id = arranger.id
              WHERE piece.id = NEW.piece_id
            )
        WHERE docid = NEW.piece_id;
    END
    """,
    """
    CREATE TRIGGER library_piece_arranger_search_update
    AFTER UPDATE ON library_piece_arranger
    FOR EACH ROW
    BEGIN
        UPDATE piece_search
        SET body = (
              SELECT
                  title || ' ' ||
                  subtitle || ' ' ||
                  comment || ' ' ||
                  GROUP_CONCAT(composer.first_name || ' ' || composer.last_name) || ' ' ||
                  GROUP_CONCAT(arranger.first_name, arranger_last_name)
              FROM library_piece AS piece
              LEFT OUTER JOIN library_piece_composer AS pc
                           ON piece.id = pc.piece_id
              LEFT OUTER JOIN library_piece_arranger AS pa
                           ON piece.id = pa.piece_id
                         JOIN library_composer AS composer
                           ON pc.composer_id = composer.id
                         JOIN library_arranger AS arranger
                           ON pa.arranger_id = arranger.id
              WHERE piece.id = NEW.piece_id
            )
        WHERE docid = NEW.piece_id;
    END
    """,
    """
    CREATE TRIGGER library_piece_arranger_search_delete
    AFTER DELETE ON library_piece_arranger
    FOR EACH ROW
    BEGIN
        UPDATE piece_search
        SET body = (
              SELECT
                  title || ' ' ||
                  subtitle || ' ' ||
                  comment || ' ' ||
                  GROUP_CONCAT(composer.first_name || ' ' || composer.last_name) || ' ' ||
                  GROUP_CONCAT(arranger.first_name, arranger_last_name)
              FROM library_piece AS piece
              LEFT OUTER JOIN library_piece_composer AS pc
                           ON piece.id = pc.piece_id
              LEFT OUTER JOIN library_piece_arranger AS pa
                           ON piece.id = pa.piece_id
                         JOIN library_composer AS composer
                           ON pc.composer_id = composer.id
                         JOIN library_arranger AS arranger
                           ON pa.arranger_id = arranger.id
              WHERE piece.id = NEW.piece_id
            )
        WHERE docid = NEW.piece_id;
    END
    """,
    """
    INSERT INTO     piece_search
                    (docid, body)
    SELECT          piece.id, piece.title || ' ' || piece.subtitle || ' ' || piece.comment || ' ' ||
                    GROUP_CONCAT(composer.first_name || ' ' || composer.last_name) || ' ' ||
                    GROUP_CONCAT(arranger.first_name || ' ' || arranger.last_name)
    FROM            library_piece AS piece
    LEFT OUTER JOIN library_piece_composer AS pc ON piece.id = pc.piece_id
    LEFT OUTER JOIN library_piece_arranger AS pa ON piece.id = pa.piece_id
    INNER JOIN      library_composer AS composer ON pc.composer_id = composer.id
    INNER JOIN      library_arranger AS arranger ON pa.arranger_id = arranger.id
    GROUP BY        piece.id
    """
]

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
