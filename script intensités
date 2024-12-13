# -- coding: utf-8 --

import os
import sys
import re
from recherche_plot import filtrer_donnees , afficher_graphique

# Lecture des données depuis le fichier







# Normalisation des intensités
def normaliser_donnees(donnees):
    # Trouver la valeur maximale en utilisant une boucle
    intensite_max = 0
    for _, intensite in donnees:
        if intensite > intensite_max:
            intensite_max = intensite

    # Évite la division par zéro en cas de liste vide
    if intensite_max == 0: 
        intensite_max = 1

    # Diviser chaque intensité par la valeur maximale
    donnees_normalisees=[] 
    for longueur, intensite in donnees :
      donnees_normalisees.append((longueur, intensite / intensite_max)); 
    return donnees_normalisees


# Organisation des données en fenêtres








# Calcul des statistiques pour chaque fenêtre
def calculer_statistiques(fenetres):
    stats = {}
    for fenetre, intensites in fenetres.items(): 
        intensites.sort()  # Trie les intensités
        if intensites:
            stats[fenetre] = {
                "nombre": len(intensites),
                "minimum": intensites[0],
                "moyenne": sum(intensites) / len(intensites),
                "maximum": intensites[-1]
            }
        else:
            stats[fenetre] = {"nombre": 0, "minimum": 0, "moyenne": 0, "maximum": 0}
    return stats

# Affichage des résultats
def afficher_resultats(stats):
    for fenetre, valeurs in sorted(stats.items()):
        print(f"Fenêtre {fenetre}:")
        print(f"  Nombre de données: {valeurs['nombre']}")
        print(f"  Minimum: {valeurs['minimum']}")
        print(f"  Moyenne: {valeurs['moyenne']:.2f}")
        print(f"  Maximum: {valeurs['maximum']}")

# Fonction principale
def main():
    if len(sys.argv) < 2:
        print("Usage : python3 intensite.py <fichier> [<pas>]")
        sys.exit(1)

    fichier = sys.argv[1] 
    if len(sys.argv) > 2 :
        pas = int(sys.argv[2])
    else : 
        pas = 10

    donnees = lire_fichier(fichier) 
    donnees_normalisees = normaliser_donnees(donnees) 
    fenetres = creer_fenetres(donnees_normalisees, pas)
    stats = calculer_statistiques(fenetres)
    afficher_resultats(stats)
    
    # Demander les bornes à l'utilisateur





    

# Point d'entrée du programme
if _name_ == "_main_":
    main()
