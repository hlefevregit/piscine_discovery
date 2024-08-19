#!/usr/bin/env python3

def famous_births(figures_dict):
    # Trier le dictionnaire par date de naissance
    sorted_figures = sorted(figures_dict.items(), key=lambda item: item[1]['date_of_birth'])
    
    # Afficher chaque entrée
    for key, value in sorted_figures:
        print(f"Name: {value['name']}, Date of Birth: {value['date_of_birth']}")

# Exemple de dictionnaire des figures historiques
figures_dict = {
    1: {'name': 'Albert Einstein', 'date_of_birth': '1879-03-14'},
    2: {'name': 'Isaac Newton', 'date_of_birth': '1643-01-04'},
    3: {'name': 'Marie Curie', 'date_of_birth': '1867-11-07'},
    4: {'name': 'Charles Darwin', 'date_of_birth': '1809-02-12'},
    5: {'name': 'Leonardo da Vinci', 'date_of_birth': '1452-04-15'}
}

# Appeler la méthode famous_births et afficher le résultat
famous_births(figures_dict)