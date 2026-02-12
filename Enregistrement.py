import os
from Utilisation import recall, authentication
from Pass import get_fernet




def action_principale():
    choix = input("Quels actions voulez-vous exécuter Enregistrer / Voir / Quitter ? (E/V/Q) : ").lower()

    if choix == "e":
        account = input("Nom du compte : ")
        password = input("Mot de passe du compte : ")
        save_password(password, account)

    elif choix == "v":
        voir_donnees()

    elif choix == "q":
        print("Fermeture du programme.")
        exit()

    else:
        print("Choix invalide.")


def save_password(password, account):
    fernet = get_fernet()
    encrypted_password = fernet.encrypt(password.encode())

    file = "données.txt"
    with open(file, "a", encoding="utf-8") as file:
        file.write(f"{account}:{encrypted_password.decode()}\n")

    print("Mot de passe enregistré avec succès.")


def voir_donnees():
    file = "données.txt"
    if not os.path.exists(file):
        print("Aucune données enregistrées.")
        return

    fernet = get_fernet()

    with open(file, "r", encoding="utf-8") as file:
        for line in file:
            account, encrypted = line.strip().split(":")
            decrypted = fernet.decrypt(encrypted.encode()).decode()
            print(f"Compte : {account} | Mot de passe : {decrypted}")

recall()


if authentication() == "Mot de passe correct, accès autorisé":
    action_principale()
else :
    print("Accès refusé.")
