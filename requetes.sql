/*
CREATE TABLE ventes (date TEXT, produit TEXT, prix INTEGER, qte INTEGER, region TEXT);
*/

/*
SELECT * FROM ventes
*/



/*
SELECT COUNT(*) FROM ventes
*/

/*
SELECT
    SUM(prix * qte) AS chiffre_affaires
FROM ventes
*/



/*
SELECT
    produit,
    SUM(prix * qte) AS total_ventes
FROM ventes
GROUP BY produit
*/




SELECT
    region,
    SUM(prix * qte) AS total_ventes
FROM ventes
GROUP BY region
ORDER BY total_ventes DESC

