-- Répertorie toutes les émissions dans hbtn_0d_tvshows avec leur genre_id (NULL si aucun genre)
USE hbtn_0d_tvshows;
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
