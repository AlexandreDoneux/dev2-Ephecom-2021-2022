# python 3.10
# UTF-8

# help est une commande permettant d'avoir des informations sur l'ensemble des commandes.
# En indiquant spécifiquement une commande (ex: '/help get_date') on aura des informations
# sur ccette commande en particulier.
# -> Ce qu'elle fait, comment l'utiliser, arguments, ...


class NoSuchCommand(Exception):
    def __init__(self):
        print("La commande indiquée n'existe pas !")


class Help:
    def __init__(self, command="all"):
        """
        :param: command: str - commande sur laquelle on veut l'aide. Si aucune n'est précisée on affiche l'aide de
                               toutes les commandes
        """
        self.command = command
        self.help_text = ""

        self.help_weather = "Aide weather \n"
        self.help_news = "Aide de la commande news \n permettant à l'utilisateur une recherche sur les articles " \
                         "du jour selon le pays disponible où il veut \n"

        self.help_itiner = "/itiner\nPermet de trouver son trajet en faisant l'estimation du temps et de la " \
                              "distance \n"

        self.help_research = "/{site} research\nCommande permettant une recherche sur {site}. research est la " \
                             "recherche, la phrase que vous voulez rechercher. \n"

        self.help_info = "Aide de la commande info\nDescription: commande permettant d'afficher des informations" \
                         " sur le module de chatbot multimédia\nUtilisation: /info\n"

        self.help_time = "Aide de la commande time\nDescription: commande permettant d'afficher l'heure au format" \
                         " anglais ou français (par défaut, l'affichage est en français)\n " \
                         "Utilisation: /time [eng ou fr]\n[]: paramètre optionnel\n"

        self.help_help = "/help [command]      []: paramètre optionnel\n Commande permettant d'afficher les aides des" \
                         " différentes commandes. 'command' représente la commande pour laquelle vous voulez de " \
                         "l'aide. Sans commande spécifié /help renvoie les aides concernant toutes les commandes."

        """
        self.help_date = "Aide de la commande date\nDescription: commande permettant d'afficher la date au format" \
                         "anglais ou français (par défaut, l'affichage est en français)\n" \
                         "Utilisation: /date [eng ou fr]\n[]: paramètre optionnel\n"
        """

        # meilleur configuration ?
        self.help_date = "/date [eng/fr]      []: paramètre optionnel\n Commande permettant d'afficher la date au" \
                         " format anglais ou français (par défaut, l'affichage est en français)\n"

        self.command_help_correspond = {"help": self.help_help, "weather": self.help_weather, "news": self.help_news,
                                        "itiner": self.help_itiner, "linkedin": self.help_research,
                                        "youtube": self.help_research, "wikipedia": self.help_research,
                                        "info": self.help_info, "time": self.help_time, "date": self.help_date}

    def __str__(self):
        """
        Fonction qui affiche l'aide de la commande demandée, ou celles de toutes les commandes si aucune n'est demandée.
        :raises: ValueError
                    - la commande demandée n'existe pas
        """

        command_keys = self.command_help_correspond.keys()
        if self.command == "all":

            for i in command_keys:
                if i in ["linkedin", "youtube", "wikipedia"]:
                    self.help_text += self.command_help_correspond[i].format(site=i) + "\n"
                else:
                    self.help_text += self.command_help_correspond[i] + "\n"

        else:
            if self.command in ["linkedin", "youtube", "wikipedia"]:
                self.help_text += self.command_help_correspond[self.command].format(site=self.command)

            elif self.command in command_keys:
                self.help_text += self.command_help_correspond[self.command]

            else:
                raise NoSuchCommand

        return self.help_text

        # Mieux faire l'exception !!!!!


if __name__ == "__main__":
    pass
