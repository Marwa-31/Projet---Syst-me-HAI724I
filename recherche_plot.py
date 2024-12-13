# -- coding: utf-8 --
#!/usr/bin/env python3
import sys
import re 
import matplotlib.pyplot as plt

#filtrage des donnees
def filtrer_donnees(donnees, borne_inf, borne_sup): 
    """
    Filtre les données pour ne garder que celles dans l'intervalle [borne_inf, borne_sup].
    """
    resultat = []
    for longueur, intensite in donnees:
        if borne_inf <= longueur <= borne_sup:
            resultat.append((longueur, intensite))
    return resultat

#l'affichage du graphique des intensités en fonction des longueurs d'onde.

def afficher_graphique(donnees_filtrees, borne_inf, borne_sup):
    """
    Affiche un graphique des intensités en fonction des longueurs d'onde.
    """
    if not donnees_filtrees:
        print(f"Aucune donnée trouvée pour l'intervalle [{borne_inf}-{borne_sup}].", file=sys.stderr)
        return

    longueurs, intensites = zip(*donnees_filtrees) # La fonction zip(*donnees_filtrees) est utilisée ici pour séparer les données filtrées en deux listes 

    plt.figure(figsize=(8, 5))
    plt.plot(longueurs, intensites, marker='o', linestyle='-', color='blue')
    plt.title(f"Intensités pour l'intervalle [{borne_inf}-{borne_sup}] nm")
    plt.xlabel("Longueur d'onde (nm)")
    plt.ylabel("Intensité (normalisee)") 
    plt.grid(True)
    plt.show()
