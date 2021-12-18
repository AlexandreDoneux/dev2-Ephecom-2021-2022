# python 3.10
# UTF-8

# Définition des classes concernant la commande de recherche sur les sites pour le bot multimedia de Ephecom

import webbrowser


def percent_encoding_url(url=""):
    """
    Fonction modifiant certains paramètres spéciaux dans un string pour permettre à ce string d'être utlisée comme url.
    :param - url: string
    :return - result_url: la nouvelle string où les caractères spéciaux ont étés changés.
            - False: lorsque le paramètre url de la fonction n'est pas un string.
    """
    dict_char_to_url_code = {"[": "%5B", "]": "%5D", "{": "%7B", "}": "%7D", "+": "%2B", "<": "%3C", ">": "%3E",
                             "&": "%26", ":": "%3A", "/": "%2F", "?": "%3F", "#": "%23", "@": "%40", "$": "%24",
                             ",": "%2C", ";": "%3B", "%": "%25", '"': "%22", "'": "%27", "!": "%21", "(": "%28",
                             ")": "%29", "*": "%2A", "=": "%3D"}
    # pour youtube, pas besoin de modifier : ",',!,(,),* -> les remplacer quand même ?
    # OUI, on en a besoin pour wikipedia
    result_url = ""

    if type(url) == str:
        for caract in url:
            if caract in dict_char_to_url_code.keys():
                result_url += dict_char_to_url_code[caract]
            else:
                result_url += caract
    else:
        return False

    return result_url


def no_blank_string_in_list(original_list):
    """
    sépare les valeurs de la liste ayant un(des) espace(s) en plusieurs éléments de la liste.
    :param - original_list: liste contenant des string
    :return - result_list: Une nouvelles liste où les valeurs de original_list possédant des espaces ont étés divisés
    en plusieurs valeurs.
    """
    # normalement on en a pas besoin dans notre application vu qu'on crée toujours les objets des commandes avec une
    # liste de strings sans espaces.

    original_list = [str(i) for i in original_list]  # on transforme toutes les valeurs de la liste originale au cas où
    result_list = []
    for i in original_list:
        result_list.extend(i.split())  # colle la liste obtenue avec split
    return result_list


class Research:
    def __init__(self, arguments):
        """
        :param: arguments : list - liste contenant l'ensemble des mots de la recherche
        :return: none
        """
        self.site = ""
        self.url = ""
        self.arguments = no_blank_string_in_list(arguments)

# Pas vraiment besoin de getter et setter, vu qu'on y accède que depuis l'interieur de la classe

    def __str__(self):
        recherche = "\'"
        for i in self.arguments:
            recherche += i + " "
        recherche = recherche[:-1]   # on enlèvre l'espace en trop ajouté à la fin.
        recherche += "\'"
        return "On fait la recherche : " + recherche + " sur le site " + self.site

    def go_to_site(self):
        """
        Ouvre un nouvel onglet du navigateur de l'utilisateur et fait la recherche voulue sur le site voulu
        :param: none
        :return: none
        :raises: ValueError
                    - si l'url est vide
        """
        if self.url == "":
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
        # self.url = ""
        self.arguments = self.arguments = no_blank_string_in_list(arguments)

    def create_url_linkedin(self):
        """
        Crée l'url de recherche spécifique à Linkedin en fonction des *arguments. Mets cette url dans l'attribut
        self.url de la classe.  Si arguments est une liste vide renvoie vers la page d'acceuil de Linkedin.
        :param: none
        :return: none
        """

        # Recherche "Charles Doneux" -> https://fr.linkedin.com/pub/dir?firstName
        # =Charles&lastName=Doneux&trk=public_profile_people-search-bar_search-submit
        if self.arguments == []:
            self.url = "https://fr.linkedin.com"
        elif len(self.arguments) != 2:
            print("Utilisez 2 arguments pour la recherche Linkedin : nom et prénom.")
            return -1
        else:
            self.url = ("https://fr.linkedin.com/pub/dir?firstName=" + '+'.join((self.arguments[0]).split()) +
                        "+&lastName=" + "+".join((self.arguments[1]).split())
                        + "&trk=public_profile_people-search-bar_search-submit")

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
        # self.url = ""
        self.arguments = self.arguments = no_blank_string_in_list(arguments)

    def create_url_wikipedia(self):
        """
        Crée l'url de recherche spécifique à Wikipedia en fonction des *arguments. Mets cette url dans l'attribut
        self.url de la classe. Si arguments est une liste vide renvoie vers la page d'acceuil de Wikipedia.
        :param: none
        :return: none
        """
        # self.url = "https://fr.wikipedia.org/w/index.php?title=Spécial:Recherche&search="

        # Meilleur type d'url : https://fr.wikipedia.org/w/index.php?search=test+unitaire&title=Spécial:Recherche
        # &profile=advanced&fulltext=1&ns0=1
        # -> ne redirige pas si l'article existe. On voit tous les résultats similaires.

        if self.arguments == []:
            self.url = "https://www.wikipedia.org"

        else:
            # self.url = "https://fr.wikipedia.org/w/index.php?title=Spécial:Recherche&search="
            self.url = "https://fr.wikipedia.org/w/index.php?search="
            for i in self.arguments:
                self.url += percent_encoding_url(i)
                if self.arguments.index(i) != len(self.arguments)-1:  # Ajoute un "+" après chaque terme sauf le dernier
                    self.url += "+"
            # self.url += "&go=Go&ns0=1"
            self.url += "&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1"


class Youtube(Research):
    def __init__(self, arguments):
        """
        :param: arguments : list - liste contenant l'ensemble des mots de la recherche
        :return: none
        """
        self.site = "Youtube"
        # self.url = ""
        self.arguments = self.arguments = no_blank_string_in_list(arguments)

    def create_url_youtube(self):
        """
        Crée l'url de recherche spécifique à Youtube en fonction des *arguments. Mets cette url dans l'attribut
        self.url de la classe. Si arguments est une liste vide renvoie vers la page d'acceuil de Youtube.
        :param: none
        :return: none
        """

        if self.arguments == []:
            self.url = "https://www.youtube.com"

        else:
            # Recherche "thomas va bien" -> https://www.youtube.com/results?search_query=thomas+va+bien
            self.url = "https://www.youtube.com/results?search_query="
            for i in self.arguments:
                self.url += percent_encoding_url(i)
                if self.arguments.index(i) != len(self.arguments)-1:  # Ajoute un "+" après chaque terme sauf le dernier
                    self.url += "+"

# Dois-je mettre l'initialisation de toutes les variables dans le init des classes enfant ?
# Ou est-ce que c'est déjà fait grâce à la classe parent ? -> apparement non


if __name__ == "__main__":
    pass
