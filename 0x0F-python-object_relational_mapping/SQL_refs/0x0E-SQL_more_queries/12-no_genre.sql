-- No genre (join)
-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT ts.title, tsg.genre_id
FROM tv_shows as ts
    LEFT JOIN tv_show_genres as tsg
    ON ts.id = tsg.show_id
WHERE tsg.genre_id IS NULL
ORDER BY title, genre_id;
