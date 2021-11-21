# python 3.10
# alexandre Doneux
# 20/11/2021

# Définition des classes concernant la commande de recherche sur les sites pour le bot multimedia de Ephecom

import webbrowser

class Research():
    def __init__(self, *arguments):
        self.site = ""
        self.url = ""
        self.arguments = list(*arguments)

# Pas vraiment besoin de getter et setter, vu qu'on y accède que depuis l'interieur de la classe

    def __str__(self):
        recherche = "\'"
        for i in self.arguments:
            recherche += i + " "
        recherche = recherche[:-1]   # on enlèvre l'espace en trop ajouté à la fin.
        recherche += "\'"
        return("On fait la recherche : " + recherche + " sur le site " + self.site)

    def go_to_site(self):
        if self.url == "":
            print("L'URL est vide")
            return(-1)
        webbrowser.open(self.url)

class Linkedin(Research):
    def __init__(self, *arguments):
        self.site = "Linkedin"
        self.url = ""
        self.arguments = list(arguments)

    def create_url_linkedin(self):
        # Recherche "Charles Doneux" -> https://fr.linkedin.com/pub/dir?firstName=Charles&lastName=Doneux&trk=public_profile_people-search-bar_search-submit
        if len(self.arguments) != 2:
            print("Utilisez 2 arguments pour la recherche Linkedin : nom et prénom.")
            return(-1)

        self.url = ("https://fr.linkedin.com/pub/dir?firstName="+self.arguments[0]+"&lastName="+self.arguments[1]+
                        "&trk=public_profile_people-search-bar_search-submit")

    # problème Linkedin : Il faut s'inscrire
    # problème d'accents dans les url

    # besoin de créer une méthode à part ? Pourquoi ne pas le faire dans le __init__ ?

class Wikipedia(Research):
    def __init__(self, *arguments):
        self.site = "Wikipedia"
        self.url = ""
        self.arguments = list(arguments)

    def create_url_wikipedia(self):
        # Recherche "repertoire courant" -> https://fr.wikipedia.org/w/index.php?title=Spécial:Recherche&search=repertoire+courant&go=Go&ns0=1
        self.url = "https://fr.wikipedia.org/w/index.php?title=Spécial:Recherche&search="
        for i in self.arguments:
            self.url += i
            if self.arguments.index(i) != len(self.arguments)-1:  # Ajoute un "+" après chaque terme sauf le dernier
                self.url += "+"
        self.url += "&go=Go&ns0=1"

class Youtube(Research):
    def __init__(self, *arguments):
        self.site = "Youtube"
        self.url = ""
        self.arguments = list(arguments)

    def create_url_youtube(self):
        # Recherche "thomas va bien" -> https://www.youtube.com/results?search_query=thomas+va+bien
        self.url = "https://www.youtube.com/results?search_query="
        for i in self.arguments:
            self.url += i
            if self.arguments.index(i) != len(self.arguments)-1 :  # Ajoute un "+" après chaque terme sauf le dernier
                self.url += "+"


# Dois-je mettre l'initialisation de toutes les variables dans le init des classes enfant ?
# Ou est-ce que c'est déjà fait grâce à la classe parent ? -> apparement non

if __name__ == "__main__" :
    ma_recherche = Wikipedia("mémoire", "partagée")

    print(ma_recherche)
    ma_recherche.create_url_wikipedia()
    ma_recherche.go_to_site()

    ma_recherche2 = Youtube("salut", "c'est", "cool")

    print(ma_recherche2)
    ma_recherche2.create_url_youtube()
    print(ma_recherche2.url)
    ma_recherche2.go_to_site()

