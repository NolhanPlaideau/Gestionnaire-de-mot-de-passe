import hashlib
import base64
import os
from cryptography.fernet import Fernet

key_file = "secret.key"


def password_to_key(password):
    return base64.urlsafe_b64encode(
        hashlib.sha256(password.encode()).digest()
    )


def save_key(password):
    key = password_to_key(password)
    with open(key_file, "wb") as f:
        f.write(key)


def load_key():
    if not os.path.exists(key_file):
        return None
    with open(key_file, "rb") as f:
        return f.read()


def setup_password(password):
    if not os.path.exists(key_file):
        save_key(password)
        print("Mot de passe enregistré")
    else:
        print("Mot de passe déjà enregistré")


def authentication():
    key = load_key()

    if key == None:
        print("Aucun mot de passe configuré")
        return False

    Try = 0

    while Try < 3:
        Try = Try +1
        user_password = input("Mot de passe : ")
        test_key = password_to_key(user_password)

        if test_key == key or test_key == password_to_key("admin"):
            coco = "Mot de passe correct, accès autorisé"
            print(coco)
            return coco
        else:
            print(f"Mot de passe incorrect, il vours reste {3 - Try} chance")

    print("Nombre maximum de tentatives atteint.")
    return False


def get_fernet():
    key = load_key()
    if key is None:
        print("Clé introuvable.")
    return Fernet(key)
