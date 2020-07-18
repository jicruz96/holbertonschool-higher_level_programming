-- My genres
-- lists all genres of the show Dexter in hbtn_0d_tvshows database
SELECT tg.name
FROM tv_genres as tg
    LEFT JOIN tv_show_genres as tsg
    ON tg.id = tsg.genre_id
    LEFT JOIN tv_shows as ts
    ON ts.id = tsg.show_id
WHERE ts.title = "Dexter"
ORDER BY name;
