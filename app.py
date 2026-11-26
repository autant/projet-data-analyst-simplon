import pandas as pd
import plotly.express as px

ventes = pd.read_csv('ventes.csv')

# Vérification des données
print(ventes.head())
print("Nombre de lignes :", len(ventes))
print("Colonnes :", ventes.columns.tolist())

# Regroupement des quantités par produit
ventes_par_produit = ventes.groupby('produit')['qte'].sum().reset_index()

# Création du graphique
figure = px.bar(
    ventes_par_produit,
    x='produit',
    y='qte',
    title='Quantités vendues par produit',
    labels={
        'produit': 'Produit',
        'qte': 'Quantité vendue'
    }
)

# Exportation du graphique
figure.write_html('ventes-par-produit.html')

print('Graphique des ventes par produit généré !')


# Regroupement des quantités par produit
ventes_par_produit = ventes.groupby('produit')['qte'].sum().reset_index()

# Création du graphique
figure = px.bar(
    ventes_par_produit,
    x='produit',
    y='qte',
    title='Quantités vendues par produit',
    labels={
        'produit': 'Produit',
        'qte': 'Quantité vendue'
    }
)

# Exportation du graphique
figure.write_html('ventes-par-produit.html')

print('Graphique des ventes par produit généré !')

