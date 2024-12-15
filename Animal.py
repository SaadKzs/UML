class Habitat:
    def __init__(self, genre):
        self.genre = genre

class Tete:
    pass

class Corps:
    pass

class Membre:
    def __init__(self, type_membre):
        self.type_membre = type_membre

class Animal:
    def __init__(self, nom, habitat):
        self.nom = nom
        self.habitat = habitat
        self.tete = Tete()  # Composition: chaque Animal a exactement une Tête
        self.corps = Corps()  # Composition: chaque Animal a exactement un Corps
        self.membres = []  # Composition: un Animal peut avoir plusieurs Membres

    def ajouter_membre(self, membre):
        self.membres.append(membre)

    def retirer_membre(self, membre):
        self.membres.remove(membre)

class Herbivore(Animal):
    pass

class Carnivore(Animal):
    pass
