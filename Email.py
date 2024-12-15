class FichierJoint:
    def __init__(self, nom, taille):
        self.nom = nom
        self.taille = taille

class Email:
    def __init__(self, titre, texte, expediteur, destinataire):
        self.titre = titre
        self.texte = texte
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.fichiers_joints = []

    def ajouter_fichier(self, fichier):
        self.fichiers_joints.append(fichier)

    def supprimer_fichier(self, fichier):
        self.fichiers_joints.remove(fichier)
