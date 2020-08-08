-- Count shows by genre
-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT
    tg.name as genre,
    tsg.genre_id as number_of_shows
FROM tv_genres as tg, tv_show_genres as tsg
WHERE tg.id = tsg.genre_id
GROUP BY tg.id
ORDER BY number_of_shows DESC;
