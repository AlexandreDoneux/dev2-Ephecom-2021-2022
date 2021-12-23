# Python 3.10
# UTF -8
import os
import platform
import subprocess

if __name__ == "__main__":
    script_path = os.path.dirname(os.path.abspath(__file__))
    script_path += "/main.py"  # Marche sur Windows, MacOS et Linux
    print(script_path)
    running = True
    while running:
        attribut = input("Entrez une commande (q pour quitter) : ")
        if attribut == 'q':
            running = False
        else:
            attributs = attribut.split()
            # Supprimes les string vides dans attributs crées par le .split à cause de nombreux espaces dans la commande
            attributs = [i for i in attributs if i != ""]
            # va regarder quel est l'os pour savoir pour les droits admin
            parameter = '-n' if platform.system().lower() == 'windows' else '-c'
            # execute la commande
            command = ['python3', script_path, '-chatbot', *attributs]
            # Rajouté le 3.10 au cas où il y a plusieurs versions disponibles sur l'ordi de l'utilisateur
            # et que 3.10 n'est pas la version par défaut?
            response = subprocess.call(command)

            if response != 0:
                print(response)
                print("Il y a un problème avec subprocess")
