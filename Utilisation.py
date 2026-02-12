import os
from Pass import authentication
from new_mdp import create_password
from Pass import setup_password

DATA_FILE = "données.txt"


def recall():
    if not os.path.exists("secret.key"):
        print("Première utilisation.")
        mdp = create_password()
        setup_password(mdp)
        return True
    else:
        print("Veuillez entrer votre mot de passe : ")
        return authentication()
