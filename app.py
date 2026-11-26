
import pandas as pd
import plotly.express as px


ventes = pd.read_csv('ventes.csv')


print(ventes.head())
print("Nombre de lignes :", len(ventes))
print("Colonnes :", ventes.columns.tolist())


# GRAPHIQUE 1 : Quantités par produit


ventes_par_produit = ventes.groupby('produit', as_index=False)['qte'].sum()

figure_ventes = px.bar(
    ventes_par_produit,
    x='produit',
    y='qte',
    title='Quantités vendues par produit',
    labels={
        'produit': 'Produit',
        'qte': 'Quantité vendue'
    }
)

figure_ventes.write_html('ventes-par-produit.html')


# GRAPHIQUE 2 : Chiffre d'affaires par produit


ventes['total'] = ventes['prix'] * ventes['qte']

ca_par_produit = ventes.groupby('produit', as_index=False)['total'].sum()

figure_ca = px.pie(
    ca_par_produit,
    values='total',
    names='produit',
    title="Chiffre d'affaires par produit"
)

figure_ca.write_html('chiffre-affaires-par-produit.html')

print("Les deux graphiques ont été générés avec succès !")
