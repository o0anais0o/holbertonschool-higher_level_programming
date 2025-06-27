-- Répertorie toutes les émissions comiques de la base de données, passées en argument.
-- Chaque enregistrement affiche : tv_shows.title
-- Les résultats sont triés par ordre croissant selon le titre de l'émission.
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
