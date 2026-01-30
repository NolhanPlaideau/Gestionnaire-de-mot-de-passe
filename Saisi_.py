import hashlib
import base64
from cryptography.fernet import Fernet

# Demande à l'utilisateur d'entrer un mot de passe
World = input("Entrez votre mot de passe : ")
# demande nom du compte
Account = input("Entrez le nom de votre compte : ")
# liste pour stocker les mots de passe 
list = []


def Enregistrer():
    resp = str(input("Voulez-vous enregistrer le mot de passe ? (oui/non) : "))
    if resp == "oui":
        save_password(World, Account)
    if resp == "non":
        print("Mot de passe non enregistré") # Demande d'enregistrement

def save_password(password, account):
    list.append("account name = " + account + ", " + "Pass world = " + password)
    print("Mot de passe enregistré") # Enregistrement du mot de passe hash





Enregistrer()
print(list)
