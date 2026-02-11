from random import randint
from Création_mot_de_passe import demande, D


def generation_mot_passe(length=10):
    """Renvoie une chaîne de  chiffres aléatoires (0-9)."""
    return ''.join(str(randint(0, 9)) for _ in range(length))

print("Première et unique exécution !")

if demande == "oui" :
    new_mdp = generation_mot_passe()
    print (new_mdp)
    print ("Mot de passe enregistré")
     
elif demande == "non" :
    new_mdp = input("entrer votre mot de passe:")
    print(new_mdp)
    print ("Mot de passe enregistré")
 
else : 
    print("veuillez répondre par 'oui' ou 'non'")
    D()


def new__mdp():
    return new_mdp