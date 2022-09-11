liste_pokemons = {
  'Bulbizarre' : (70, 7),
  'Herbizarre' : (100,13),
  'Abo' : (200, 7),
  'Pikachu' : (40, 6)
}

liste_pokemons["Goupil"] = (60,10)
print(liste_pokemons)

def le_plus_grand(pokemons):
  grand = ''
  taille_max = 0
  for (nom,(taille, poids)) in pokemons.items():
        if taille > taille_max:
            taille_max = taille
            grand = nom
  return("Le plus grand pokémon est " + grand + ". Il mesure " + str(taille_max) + " cm.")
le_plus_grand(liste_pokemons)

def le_plus_leger(pokemons):
  leger = ''
  poids_max = 10000
  for (nom,(taille, poids)) in pokemons.items():
        if poids < poids_max:
            poids_max = poids
            leger = nom
  return("Le pokémon le plus léger est " + leger + ". Il pèse " + str(poids_max) + " kg.")
le_plus_leger(liste_pokemons) 

def taille(pokemons, nom_pokemon):
    return "La taille de " + nom_pokemon + " est de " + str(pokemons[nom_pokemon][0]) + " cm"
    
def tailleV2(pokemons, nom_pokemon):
    resultat = "None"
    for nom in pokemons.keys():
        if pokemons[nom] == nom_pokemon :
            resultat = "La taille de " + nom_pokemon + " est de " + str(pokemons[nom_pokemon][0]) + " cm"
    return resultat
    
def tailleV3(pokemons, nom_pokemon):
    if pokemons[nom_pokemon] != "":
        return "La taille de " + nom_pokemon + " est de " + str(pokemons[nom_pokemon][0]) + " cm"
    else:
        return None