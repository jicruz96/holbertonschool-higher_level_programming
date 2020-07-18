-- Comedy only
-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT ts.title
FROM tv_shows as ts
    RIGHT JOIN tv_show_genres as tsg
    ON ts.id = tsg.show_id
    LEFT JOIN tv_genres as tg
    ON tsg.genre_id = tg.id
WHERE tg.name = "Comedy"
ORDER BY title;
