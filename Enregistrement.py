from cryptography.fernet import Fernet
import os
from Création_mot_de_passe import recall


password = ""
account = ""


# DEMANDE ACTION PRINCIPALE
def action_principale():
    requête = input("Voulez-vous enregistrer/Voir les données d'un compte ? (E/V) : ").lower()

    if requête == "e":
        # SAISIE UTILISATEUR
        password = input("Entrez votre mot de passe : ")
        account = input("Entrez le nom de votre compte : ")

        enregistrer()
    elif requête == "v":
        with open("données.txt", "r", encoding="utf-8") as file:
            print(file.read())
    else:
        print("Veuillez répondre par 'E' ou 'V'")
        action_principale()

# ENREGISTREMENT
def enregistrer():
    resp = input("Voulez-vous enregistrer le mot de passe ? (oui/non) : ").lower()
    if resp == "oui":
        save_password(password, account)
    else:
        print("Fermeture du programme")
        exit()

# SAUVERGARDER LE MOT DE PASSE CHIFFRÉ
def save_password(password, account):
    from Pass import fernet
    encrypted_password = fernet.encrypt(password.encode())

    with open("données.txt", "a", encoding="utf-8") as file:
        file.write(f"Compte : {account}\n")
        file.write(f"Mot de passe chiffré : {encrypted_password.decode()}\n")
        file.write("-" * 30 + "\n")

    print("Mot de passe chiffré et enregistré avec succès")


if recall("Access Granted") == "allow":
    action_principale()
    save_password(password, account)

else:
    print("Réessayer")
    recall()
