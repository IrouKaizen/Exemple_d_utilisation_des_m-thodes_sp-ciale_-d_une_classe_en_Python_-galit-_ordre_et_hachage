# Définition de la classe Personne avec deux attributs : nom et âge
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    # Définition de la méthode spéciale pour l'égalité entre deux Personnes
    def __eq__(self, other):
        return self.nom == other.nom and self.age == other.age
    
    # Définition de la méthode spéciale pour l'ordre entre deux Personnes
    def __lt__(self, other):
        return self.age < other.age
    
    # Définition de la méthode spéciale pour la valeur de hachage d'une Personne
    def __hash__(self):
        return hash((self.nom, self.age))

# Création de quatre objets Personne
personne1 = Personne("Alice", 30)
personne2 = Personne("Bob", 25)
personne3 = Personne("Charlie", 35)
personne4 = Personne("Charlie", 35)

# Stockage des Personnes dans une liste et tri de la liste par ordre d'âge
personnes = [personne1, personne2, personne3, personne4]
personnes_triees = sorted(personnes)

# Stockage des Personnes dans un ensemble pour éliminer les doublons
personnes_ensemble = set(personnes)

# Comparaison de deux Personnes avec l'opérateur ==
print(personne1 == personne2)
print(personne1 == Personne("Alice", 30))
