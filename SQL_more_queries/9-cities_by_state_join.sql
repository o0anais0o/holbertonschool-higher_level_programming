-- Répertorie toutes les villes avec leur état, en utilisant une seule instruction SELECT et un JOIN
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
