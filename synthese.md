Fiche synthèse – Analyse des ventes

1. Objectif de l'analyse
L'objectif de cette analyse est d'étudier les données commerciales afin d'identifier les produits qui génèrent le plus de ventes et de chiffre d'affaires, ainsi que les performances commerciales par région.

L'analyse porte sur un fichier CSV contenant 39 enregistrements de ventes, répartis sur trois produits et deux régions : Nord et Sud.

2. Résultats de l'analyse SQL
3.a – Chiffre d'affaires total
Le chiffre d'affaires global est calculé en multipliant le prix unitaire par la quantité vendue, puis en additionnant les résultats.
44 825 €
Chiffre d'affaires total réalisé

3.b – Analyse des ventes par produit
Produit	Quantités vendues	Chiffre d'affaires
Produit A	1 750	17 500 €
Produit B	1 055	15 825 €
Produit C	575	11 500 €
Total	3 380	44 825 €

Constats :
- Le produit A est le plus vendu avec 1 750 unités.
- Le produit A génère également le chiffre d'affaires le plus important.
- Le produit C est le moins vendu, avec 575 unités.
- Le produit B présente un chiffre d'affaires intermédiaire.

3.c – Analyse du chiffre d'affaires par région
Région	Chiffre d'affaires
Sud	24 100 €
Nord	20 725 €
Total	44 825 €

Constats :
- La région Sud réalise le chiffre d'affaires le plus élevé avec 24 100 €, soit environ 53,8 % du chiffre d'affaires total.
- La région Nord représente 20 725 €, soit environ 46,2 %.
- La région Sud dépasse la région Nord de 3 375 €, soit environ 16,3 %.



3. Analyse des graphiques Python
Deux graphiques interactifs ont été réalisés avec les bibliothèques Pandas et Plotly :
- Graphique 1 : représentation des quantités vendues pour chaque produit.
- Graphique 2 : représentation de la répartition du chiffre d'affaires entre les produits.
Ces graphiques facilitent la comparaison des performances commerciales et rendent les résultats plus lisibles.

4. Conclusion générale
L'analyse montre que le produit A est le principal contributeur aux ventes, aussi bien en volume qu'en chiffre d'affaires.

Le produit B occupe la deuxième position, tandis que le produit C représente le volume de ventes le plus faible.

Cette étude permet de mieux comprendre la répartition des ventes et d'identifier les produits les plus performants. Elle constitue une première base pour orienter les décisions commerciales, notamment en matière de gestion des stocks et de stratégie de vente.