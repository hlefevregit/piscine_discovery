#!/usr/bin/env python3

def find_the_redheads(family_dict):
    # Utiliser filter pour rassembler les prénoms des individus aux cheveux roux
    redheads = list(filter(lambda name: family_dict[name].lower() == 'red', family_dict.keys())).tolist()
    return redheads

# Exemple de dictionnaire des membres de la famille
family_dict = {
    'John': 'brown',
    'Jane': 'red',
    'Alice': 'blonde',
    'Bob': 'red',
    'Charlie': 'black'
}

# Appeler la méthode find_the_redheads et obtenir le résultat
redheads_list = find_the_redheads(family_dict)

# Afficher le résultat
print(redheads_list)