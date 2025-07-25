-- Répertorie tous les genres de la série Dexter à partir de la base de données passée en argument.
-- Chaque enregistrement affiche : tv_genres.name
-- Les résultats sont triés par ordre croissant selon le nom du genre.
SELECT tv_genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
