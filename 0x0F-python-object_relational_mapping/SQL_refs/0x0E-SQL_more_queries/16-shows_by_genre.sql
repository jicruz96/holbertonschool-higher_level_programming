-- Shows by genre
-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT ts.title, tg.name
FROM tv_shows as ts
    LEFT JOIN tv_show_genres as tsg
    ON ts.id = tsg.show_id
    LEFT JOIN tv_genres as tg
    ON tsg.genre_id = tg.id
ORDER BY title, name;
