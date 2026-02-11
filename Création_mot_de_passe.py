import os
from Pass import acces_control 

fichier = "données.txt"
demande =""


def D():
    demande = input("Voulez-vous générer un mot de passe ? (oui/non) : ").lower()
    return demande

def recall():
    if os.path.exists(fichier):
        print("Entrer le mot de passe pour accéder au programme :")
        acces_control(input("Mot de passe : "))

    # Génération du mot de passe
    demande = D()



# Créer le fichier pour empécher prochaine éxécution
with open(fichier, "w") as f:
    f.write("Programme déjà utilisé.")



