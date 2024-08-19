#!/usr/bin/env python3

def average(scores_dict):
    # Calculer la moyenne des scores
    total_score = sum(scores_dict.values())
    number_of_students = len(scores_dict)
    
    if number_of_students == 0:
        return 0  # Eviter la division par zéro
    
    class_average = total_score / number_of_students
    return class_average

# Exemple de dictionnaire des scores des étudiants
scores_dict = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'Diana': 90,
    'Edward': 88
}

# Appeler la méthode average et obtenir le résultat
class_average_score = average(scores_dict)

# Afficher le résultat
print(f"La moyenne de la classe est: {class_average_score:.2f}")