# python 3.10
# UTF-8
class ShowInfo:
    def __init__(self):
        """
        Fonction appelée à la création de la class info
        """
        self.__sentence_version = "Version du module : 1.0"
        self.__sentence_collaborator = "A.Doneux | K.Keurvels | S.F.Kouhave | A.D.Hakizimana"
        self.__sentence_description = "Ce module permet d'avoir différentes informations dites multimédia.\nPar " \
                                      "exemple, connaître la météo d'un certain endroit, ou avoir un lien " \
                                      "vers un itinéraire entre 2 points ou encore, faire rapidement une recherche " \
                                      "Youtube, Linkedin,..."
        self.__sentence__context = "Cela a été réalisé dans le but d'un projet informatique dans le cadre du cours " \
                                   "de développement informatique 2 à l'EPHEC de Louvain-la-Neuve."

    def __str__(self):
        """
        Fonction appelée quand on veut afficher les informations du module
        :return: une String contenant les informations du module
        """
        return self.__sentence_version + "\n--------------------------------------------------------------\n" + \
            self.__sentence_description + "\n\n" + \
            self.__sentence__context + "\n--------------------------------------------------------------\n" \
            + "Créé par " + self.__sentence_collaborator


"""help_info = "Aide de la commande info\nDescription: commande permettant d'afficher des informations sur le module" \
            " de chatbot multimédia\nUtilisation: /info\n"
print(help_info)"""
