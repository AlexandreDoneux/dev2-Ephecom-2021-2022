from unittest import TestCase
from help import Help


class TestHelp(TestCase):
    def test__str__(self):
        help_test = Help()
        self.assertEqual("Aide weather \n\nAide news \n\nAide Itinerary \n\n/linkedin research\nCommande permettant une recherche sur linkedin. research est la "
                         "recherche, la phrase que vous voulez rechercher. \n\n/youtube research\nCommande permettant une recherche sur youtube. research est la "
                         "recherche, la phrase que vous voulez rechercher. \n\n/wikipedia research\nCommande permettant une recherche sur wikipedia. research est la "
                         "recherche, la phrase que vous voulez rechercher. \n\nAide restaurant \n\nAide de la commande info\nDescription: commande permettant d'afficher "
                         "des informations sur le module de chatbot multimédia\nUtilisation: /info\n\nAide de la commande time\nDescription: commande permettant d'afficher "
                         "l'heure au format anglais ou français (par défaut, l'affichage est en français)\n Utilisation: /time [eng ou fr]\n[]: paramètre optionnel\n\n"
                         "/date [eng/fr]      []: paramètre optionnel\n Commande permettant d'afficher la date au format anglais ou français (par défaut, l'affichage"
                         " est en français)\n\n", str(help_test))

#        help_test = Help("youtube")
#        self.assertEqual("/youtube research\nCommande permettant une recherche sur youtube. research est la "
#                         "recherche, la phrase que vous voulez rechercher. \n", str(help_test))

#        help_test = Help("linkedin")
#        self.assertEqual("/linkedin research\nCommande permettant une recherche sur linkedin. research est la "
#                         "recherche, la phrase que vous voulez rechercher. \n", str(help_test))

        help_test = Help("news")
        self.assertEqual("Aide news \n", str(help_test))

        help_test = Help("time")
        self.assertEqual("Aide de la commande time\nDescription: commande permettant d'afficher l'heure au format anglais"
                         " ou français (par défaut, l'affichage est en français)\n Utilisation: /time [eng ou fr]\n[]: "
                         "paramètre optionnel\n", str(help_test))

        #help_test = Help("news", "time")
#        self.assertEqual(TypeError, Help("news", "time"))


# Problème avec wikipedia, linkedin et youtube -> apparement aucun texte n'est généré
# dans le cas ou on mets plusieurs paramètres ? -> gérer ça avant? dans la classe ?
