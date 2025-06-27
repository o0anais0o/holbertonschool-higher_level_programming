-- Crée la table unique_id avec id comme unique et la valeur par défaut 1
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
