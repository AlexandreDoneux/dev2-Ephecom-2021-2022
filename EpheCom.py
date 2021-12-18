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
            attributs = attribut.split(' ')
            # va regarder quel est l'os pour savoir pour les droits admin
            parameter = '-n' if platform.system().lower() == 'windows' else '-c'
            # execute la commande
            command = ['python3', script_path, '-chatbot', *attributs]
            response = subprocess.call(command)
            if response != 0:
                print("Il y a un problème avec subprocess")
