# python 3.10
# UTF-8

# Définition des classes concernant la commande de recherche sur les sites pour le bot multimedia de Ephecom

import webbrowser

dict_char_to_url_code = {"'": "%27", '"': "%22",  "[": "%5B", "]": "%5D", "{": "%7B", "}": "%7D", "+": "%2B",
                         "<": "%3C", ">": "%3E", "&": "%26"}


class Research:
    def __init__(self, arguments):
        """
        :param: arguments : list - liste contenant l'ensemble des mots de la recherche
        :return: none
        """
        self.site = ""
        # self.url = ""
        self.arguments = arguments

# Pas vraiment besoin de getter et setter, vu qu'on y accède que depuis l'interieur de la classe

    def __str__(self):
        recherche = "\'"
        for i in self.arguments:
            recherche += i + " "
        recherche = recherche[:-1]   # on enlèvre l'espace en trop ajouté à la fin.
        recherche += "\'"
        return("On fait la recherche : " + recherche + " sur le site " + self.site)

    def go_to_site(self):
        """
        Ouvre un nouvel onglet du navigateur de l'utilisateur et fait la recherche voulue sur le site voulu
        :param: none
        :return: none
        :raises: ValueError
                    - si l'url est vide
        """
        if self.url == "":
            print("L'URL est vide")
            return -1
        try:
            webbrowser.open(self.url)  # besoin d'un controle d'erreur
        except:
            print("Problème de connexion. Nous ne pouvons pas joindre l'url")

        # Mieux faire le contrôle d'erreurs. Dois-je mettre un contrôle sur le problème de connexion ? Normalement non.
        # webbrowser ouvre seulement le navigateur et lance la recherche. Si il n'y a pas de connexion python ne peut
        # pas s'en rendre compte

# ----------------------------------


class Linkedin(Research):
    def __init__(self, arguments):
        """
        :param: arguments : list - liste contenant l'ensemble des mots de la recherche
        :return: none
        """
        self.site = "Linkedin"
        self.url = ""
        self.arguments = arguments

    def create_url_linkedin(self):
        """
        Crée l'url de recherche spécifique à Linkedin en fonction des *arguments. Mets cette url dans l'attribut
        self.url de la classe
        :param: none
        :return: none
        """

        # Recherche "Charles Doneux" -> https://fr.linkedin.com/pub/dir?firstName
        # =Charles&lastName=Doneux&trk=public_profile_people-search-bar_search-submit
        if len(self.arguments) != 2:
            print("Utilisez 2 arguments pour la recherche Linkedin : nom et prénom.")
            return -1

        self.url = ("https://fr.linkedin.com/pub/dir?firstName="+'+'.join((self.arguments[0]).split())+"+&lastName=" +
                    "+".join((self.arguments[1]).split())+"&trk=public_profile_people-search-bar_search-submit")

    # problème Linkedin : Il faut s'inscrire
    # problème d'accents dans les url

    # besoin de créer une méthode à part ? Pourquoi ne pas le faire dans le __init__ ?


class Wikipedia(Research):
    def __init__(self, arguments):
        """
        :param: arguments : list - liste contenant l'ensemble des mots de la recherche
        :return: none
        """
        self.site = "Wikipedia"
        self.url = ""
        self.arguments = arguments

    def create_url_wikipedia(self):
        """
        Crée l'url de recherche spécifique à Wikipedia en fonction des *arguments. Mets cette url dans l'attribut
        self.url de la classe
        :param: none
        :return: none
        """

        # Recherche "repertoire courant" -> https://fr.wikipedia.org/w/index.php?title=
        # Spécial:Recherche&search=repertoire+courant&go=Go&ns0=1
        self.url = "https://fr.wikipedia.org/w/index.php?title=Spécial:Recherche&search="
        for i in self.arguments:
            self.url += i
            if self.arguments.index(i) != len(self.arguments)-1:  # Ajoute un "+" après chaque terme sauf le dernier
                self.url += "+"
        self.url += "&go=Go&ns0=1"


class Youtube(Research):
    def __init__(self, arguments):
        """
        :param: arguments : list - liste contenant l'ensemble des mots de la recherche
        :return: none
        """
        self.site = "Youtube"
        self.url = ""
        self.arguments = arguments

    def create_url_youtube(self):
        """
        Crée l'url de recherche spécifique à Youtube en fonction des *arguments. Mets cette url dans l'attribut
        self.url de la classe
        :param: none
        :return: none
        """

        # Recherche "thomas va bien" -> https://www.youtube.com/results?search_query=thomas+va+bien
        self.url = "https://www.youtube.com/results?search_query="
        for i in self.arguments:
            self.url += i
            if self.arguments.index(i) != len(self.arguments)-1:  # Ajoute un "+" après chaque terme sauf le dernier
                self.url += "+"

        # Remplacement ne marche pas
        for i in dict_char_to_url_code.keys():
            self.url.replace(i, dict_char_to_url_code[i])


# Dois-je mettre l'initialisation de toutes les variables dans le init des classes enfant ?
# Ou est-ce que c'est déjà fait grâce à la classe parent ? -> apparement non

if __name__ == "__main__":
    """
    ma_recherche = Wikipedia("mémoire", "partagée")

    print(ma_recherche)
    ma_recherche.create_url_wikipedia()
    ma_recherche.go_to_site()

    """
    ma_recherche2 = Youtube("salut", "c'est", "cool")

    print(ma_recherche2)
    ma_recherche2.create_url_youtube()
    print(ma_recherche2.url)
    ma_recherche2.go_to_site()
    
    """
    a = "https://www.youtube.com/results?search_query=salut+c'est+cool"
    b = a.replace("'", "%27")
    print(a,b)

    
    ma_recherche2 = Wikipedia("mémoire")
    ma_recherche2.create_url_wikipedia()
    ma_recherche2.go_to_site()
    """
# idées d'autres sites
