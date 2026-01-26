import hashlib

# Demande à l'utilisateur d'entrer un mot de passe
World = input("Entrez votre mot de passe : ")
# demande nom du compte
Account = input("Entrez le nom de votre compte : ")
# liste pour stocker les mots de passe 
list = []

def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest() # mot de passe => hash

def save_password(password, account):
    hash_value = hash_password(password)

    list.append("Account name = " + account + ", " + "Password = " + hash_value)

    print("Mot de passe enregistré") # Enregistrement du hash du mot de passe

def Enregistrer():
    resp = str(input("Voulez-vous enregistrer le mot de passe ? (oui/non) : "))
    if resp == "oui":
        save_password(World, Account)
    if resp == "non":
        print("Mot de passe non enregistré") # Demande d'enregistrement

Enregistrer()
print(list)
