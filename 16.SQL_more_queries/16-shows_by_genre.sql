-- Liste toutes les émissions et tous les genres associés à cette émission depuis la base de données passée en argument.
-- Si une émission n'a pas de genre, affiche NULL dans la colonne genre.
-- Chaque enregistrement affiche : tv_shows.title - tv_genres.name
-- Les résultats sont triés par ordre croissant selon le titre de l'émission et le nom du genre.
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
