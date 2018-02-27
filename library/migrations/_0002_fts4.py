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
                  GROUP_CONCAT(arranger.first_name, arranger.last_name)
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
                  GROUP_CONCAT(arranger.first_name, arranger.last_name)
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
                  GROUP_CONCAT(arranger.first_name, arranger.last_name)
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
                  GROUP_CONCAT(arranger.first_name, arranger.last_name)
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
                  GROUP_CONCAT(arranger.first_name, arranger.last_name)
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
                  GROUP_CONCAT(arranger.first_name, arranger.last_name)
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

