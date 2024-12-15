class Dossier:
    def __init__(self, etat_civil, coordonnees):
        self.etat_civil = etat_civil
        self.coordonnees = coordonnees

class Eleve:
    def __init__(self, nom, prenom, age, dossier):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.dossier = dossier

class Professeur:
    def __init__(self, nom, prenom, matiere, dossier):
        self.nom = nom
        self.prenom = prenom
        self.matiere = matiere
        self.dossier = dossier

class Classe:
    def __init__(self, professeur):
        self.professeur = professeur
        self.eleves = []

    def ajouter_eleve(self, eleve):
        self.eleves.append(eleve)

    def retirer_eleve(self, eleve):
        self.eleves.remove(eleve)
