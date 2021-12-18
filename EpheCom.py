# Python 3.10
# UTF -8
import os
import platform
import subprocess
if __name__ == "__main__":
    script_path = os.path.dirname(os.path.abspath(__file__))
    script_path += "\\main.py"
    running = True
    while running:
        attribut = input("Entrez une commande (-1 pour quitter) : ")
        if attribut == '-1':
            running = False
        else:
            # va regarder quel est l'os pour savoir pour les droits admin
            parameter = '-n' if platform.system().lower() == 'windows' else '-c'
            # execute la commande
            command = ['python3', script_path, '-chatbot', attribut]
            response = subprocess.call(command)
            if response != 0:
                print("Il y a un problème avec subprocess")
