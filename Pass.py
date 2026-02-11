import hashlib
import base64
import os
from cryptography.fernet import Fernet, InvalidToken
from new_mdp import new_mdp

# Mot de passe, issu de l'autre programme
password = new_mdp
fernet = None

def password_to_key(password):
    return base64.urlsafe_b64encode(
        hashlib.sha256(password.encode()).digest()
    )

# GESTION DE LA CLÉ DE CHIFFREMENT
def load_key():
    if not os.path.exists("secret.key"):
        key = Fernet.password_to_key(new_mdp)
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    return key



def pass_():

    # Clé basée sur le mot de passe maître
    key = load_key()
    fernet = Fernet(key)

    # On chiffre un message test
    message = "Access Granted"
    encrypted = fernet.encrypt(message.encode())

    # Vérification utilisateur
    user_password = input("Mot de passe : ")
    key2 = load_key()
    fernet2 = Fernet(key2)

    try:
        decrypted = fernet2.decrypt(encrypted).decode()
        print(decrypted)
        return True
    except InvalidToken:
        print("Mot de passe incorrect !")
        return False

pass_()

