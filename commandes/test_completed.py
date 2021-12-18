# python 3.10
# UTF-8
import unittest
import datetime

import get_date
import get_time
from get_date import Date
from get_time import Time
from get_clean_command import give_good_command
from show_info import ShowInfo
from get_news import News
from get_news import Color
from help import Help
from site_search import Youtube, Linkedin, Wikipedia


# test_unit_kevin
class DateTest(unittest.TestCase):
    def test_fr(self):
        """Vérification de l'affichage de la date en français"""
        self.assertEqual(Date(True, datetime.date(2021, 12, 2)).__str__(), "Nous sommes jeudi le 02 decembre 2021",
                         "Date(True, datetime.date(2021, 12, 2)).__str__()")

    def test_eng(self):
        """Vérification de l'affichage de la date en anglais"""
        self.assertEqual(Date(False, datetime.date(2021, 12, 2)).__str__(), "We are Thursday the 02th of December 2021",
                         "Date(False, datetime.date(2021, 12, 2)).__str__()")

    def test_number(self):
        """Vérification de l'affichage de la date avec le boolean valant un nombre"""
        self.assertRaises(TypeError, get_date.Date, 2)

    def test_String(self):
        """Vérification de l'affichage de la date avec le boolean valant un chaine de caractéres"""
        self.assertRaises(TypeError, get_date.Date, "Erreur")


class TimeTest(unittest.TestCase):
    def test_fr(self):
        """Vérification de l'affichage de l'heure en français"""
        self.assertEqual(Time(True, datetime.time(18, 45)).__str__(), "Il est 18:45",
                         "Date(True, datetime.date(2021, 12, 2))")

    def test_eng(self):
        """Vérification de l'affichage de l'heure en anglais"""
        self.assertEqual(Time(False, datetime.time(18, 45)).__str__(), "It's 6:45 PM",
                         "Date(False, datetime.date(2021, 12, 2))")

    def test_number(self):
        """Vérification de l'affichage de l'heure avec le boolean valant un nombre"""
        self.assertRaises(TypeError, get_time.Time, 2)

    def test_String(self):
        """Vérification de l'affichage de l'heure avec le boolean valant un chaine de caractéres"""
        self.assertRaises(TypeError, get_time.Time, "Erreur")


class ShowInfoTest(unittest.TestCase):
    def test_info(self):
        response = "Version du module : 1.0" + "\n--------------------------------------------------------------\n" + \
                    "Ce module permet d'avoir différentes informations dites multimédia.\nPar " \
                    "exemple, connaître la météo d'un certain endroit, ou avoir un lien " \
                    "vers un itinéraire entre 2 points ou encore, faire rapidement une recherche " \
                    "Youtube, Linkedin,..." + "\n\n" + \
                    "Cela a été réalisé dans le but d'un projet informatique dans le cadre du cours " \
                    "de développement informatique 2 à l'EPHEC de Louvain-la-Neuve." \
                    "\n--------------------------------------------------------------\n" \
                    "Créé par " + "A.Doneux | K.Keurvels | S.F.Kouhave | A.D.Hakizimana"
        """Vérification de l'affichage des informations"""
        self.assertEqual(ShowInfo().__str__(), response, "ShowInfo().__str__()")


class GoodCommandTest(unittest.TestCase):
    def test_digit(self):
        """Vérification de good_command avec un nombre passé en paramètre"""
        self.assertEqual(give_good_command('2'), '2', "give_good_command(2)")

    def test_string(self):
        """Vérification de good_command avec un nombre passé en paramètre"""
        self.assertEqual(give_good_command("/éèëêàâäçîïôöûüÿ"), "/"
                         "eeeeaaaciioouuy", "give_good_command('/éèëêàâäçîïôöûüÿ')")
    def test_boolean(self):
        """Vérification de good_command avec un nombre passé en paramètre"""
        self.assertEqual(give_good_command(True), 'true')


# test_news
class NewsTest(unittest.TestCase):
    def test_Color(self):
        """
        Test pour la class des couleurs pour chaque attribue se trouvant dans la class Color
        :return:Il retourne une phrase ou un mot qui est modifier en gras ou en couleur
        """
        self.assertEqual(Color.RED + "Hakizimana" + Color.END, "[91mHakizimana[0m")
        self.assertNotEqual(Color.RED+"Article"+Color.RED, "Article")
        self.assertEqual(Color.UNDERLINE+"Article du jour"+Color.END, "[4mArticle du jour[0m")

    def test__init__news(self):
        """
        #Test dans l'initialisation de la class News
        :return:Il retourne rien
        """
        n1 = News("be", 1)
        self.assertEqual(n1.news_of_to_day(), None)

    def test_codeNational_caracter(self):
        """
        #Il va verifier l'affichage dans la class avec un retour d'une chaine de caractère
        :return:
        """
        self.assertRaises(Exception, "Le code national doit être une chaine de caractère!")
        self.assertRaises(Exception, "Le nombre doit être une chiffre !")

    def national_code_is_string(self):
        """
        Retourne un boolean si le code est bien une chaine de caractére
        ou si number est un chiffre
        :return:
        """
        self.assertTrue(News("be", 2), News("be", 2).code in str)
        self.assertTrue(News("fr", 12), News("fr", 12).number in int)

# manque test_help et test_api_end_point


class HelpTest(unittest.TestCase):

    """ # à faire quand j'ai toutes les descriptions
    def test_help_all(self):
        result =""
        self.assertEqual(result, Help().help_text)
    """

    def test_help_date(self):
        """
        teste les string qui sera renvoyé lors d'un print d'un objet Help avec une commande qui existe: date
        """
        result = "/date [eng/fr]      []: paramètre optionnel\n Commande permettant d'afficher la date au format " \
                 "anglais ou français (par défaut, l'affichage est en français)\n"
        self.assertEqual(result, str(Help("date")))

    def test_help_itiner(self):
        """
        teste les string qui sera renvoyé lors d'un print d'un objet Help avec une commande qui existe: itiner
        """
        result = "/itiner\nPermet de trouver son trajet en faisant l'estimation du temps et de la distance \n"
        self.assertEqual(result, str(Help("itiner")))

    def test_help_youtube(self):
        """
        teste les string qui sera renvoyé lors d'un print d'un objet Help avec une commande qui existe: youtube
        """
        result = "/youtube research\nCommande permettant une recherche sur youtube. research est la recherche, la " \
                 "phrase que vous voulez rechercher. \n"
        self.assertEqual(result, str(Help("youtube")))

    def test_help_wikipedia(self):
        """
        teste les string qui sera renvoyé lors d'un print d'un objet Help avec une commande qui existe: wikipedia
        """
        result = "/wikipedia research\nCommande permettant une recherche sur wikipedia. research est la recherche, " \
                 "la phrase que vous voulez rechercher. \n"
        self.assertEqual(result, str(Help("wikipedia")))

    def test_wrong_command(self):
        """
        teste les string qui sera renvoyé lors d'un print d'un objet Help avec une commande qui n'existe pas.
        Dans ce cas, à la création de l'objet une eexception NoSuchCommand doit être raise.
        """
        self.assertRaises(Exception, Help(), "testing")


class YoutubeTest(unittest.TestCase):
    def test_youtube_url_one_arg(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string
        """
        my_youtube = Youtube(["salut"])
        my_youtube.create_url_youtube()
        self.assertEqual(my_youtube.url, "https://www.youtube.com/results?search_query=salut")

    def test_youtube_url_one_arg_apostrophe(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant une apostrophe
        """
        my_youtube = Youtube(["l'avancement"])
        my_youtube.create_url_youtube()
        self.assertEqual(my_youtube.url, "https://www.youtube.com/results?search_query=l%27avancement")

    def test_youtube_url_one_arg_apostrophe_2(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant deux apostrophes
        """
        my_youtube = Youtube(["c'es't"])
        my_youtube.create_url_youtube()
        self.assertEqual(my_youtube.url, "https://www.youtube.com/results?search_query=c%27es%27t")

    def test_youtube_url_one_arg_space(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant un espace
        """
        my_youtube = Youtube(["bonjour monsieur"])
        my_youtube.create_url_youtube()
        self.assertEqual(my_youtube.url, "https://www.youtube.com/results?search_query=bonjour+monsieur")

    def test_youtube_url_one_arg_space_2(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant deux espaces
        """
        my_youtube = Youtube(["alex est cool"])
        my_youtube.create_url_youtube()
        self.assertEqual(my_youtube.url, "https://www.youtube.com/results?search_query=alex+est+cool")

    def test_youtube_url_one_arg_plus(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string contenant un plus
        """
        my_youtube = Youtube(["a+b"])
        my_youtube.create_url_youtube()
        self.assertEqual(my_youtube.url, "https://www.youtube.com/results?search_query=a%2Bb")

    def test_youtube_url_one_arg_equal(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string contenant un symbole égal
        """
        my_youtube = Youtube(["a=b"])
        my_youtube.create_url_youtube()
        self.assertEqual(my_youtube.url, "https://www.youtube.com/results?search_query=a%3Db")

    def test_youtube_url_two_args(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec deux valeurs string
        """
        my_youtube = Youtube(["bonjour", "monsieur"])
        my_youtube.create_url_youtube()
        self.assertEqual(my_youtube.url, "https://www.youtube.com/results?search_query=bonjour+monsieur")

    def test_youtube_url_two_args_space(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec deux valeurs string dont une avec un espace
        """
        my_youtube = Youtube(["bonjour monsieur", "Obama"])
        my_youtube.create_url_youtube()
        self.assertEqual(my_youtube.url, "https://www.youtube.com/results?search_query=bonjour+monsieur+Obama")

    def test_youtube_url_two_args_plus(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec deux valeurs string dont une avec un symbole
        plus.
        """
        my_youtube = Youtube(["salut", "a+b"])
        my_youtube.create_url_youtube()
        self.assertEqual(my_youtube.url, "https://www.youtube.com/results?search_query=salut+a%2Bb")

    def test_youtube_url_one_arg_bracket_type1(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant un { et un }
        """
        my_youtube = Youtube(["alex{tom}"])
        my_youtube.create_url_youtube()
        self.assertEqual(my_youtube.url, "https://www.youtube.com/results?search_query=alex%7Btom%7D")


    def test_youtube_url_one_arg_bracket_type2(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant un [ et un ]
        """
        my_youtube = Youtube(["alex[tom]"])
        my_youtube.create_url_youtube()
        self.assertEqual(my_youtube.url, "https://www.youtube.com/results?search_query=alex%5Btom%5D")

    def test_youtube_url_one_arg_star(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant un *
        """
        my_youtube = Youtube(["étoile*"])
        my_youtube.create_url_youtube()
        self.assertEqual(my_youtube.url, "https://www.youtube.com/results?search_query=étoile%2A")

    def test_youtube_url_one_arg_hashtag(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant un #
        """
        my_youtube = Youtube(["hash#tag"])
        my_youtube.create_url_youtube()
        self.assertEqual(my_youtube.url, "https://www.youtube.com/results?search_query=hash%23tag")

    def test_youtube_url_no_arg(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments vide
        """
        my_youtube = Youtube([])
        my_youtube.create_url_youtube()
        self.assertEqual(my_youtube.url, "https://www.youtube.com")

    def test_youtube_url_one_arg_empty_string(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string vide. create_url interprète ça comme
        une liste vide
        """
        my_youtube = Youtube([""])
        my_youtube.create_url_youtube()
        self.assertEqual(my_youtube.url, "https://www.youtube.com")


class WikipediaTest(unittest.TestCase):
    def test_wikipedia_url_one_arg(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string
        """
        my_wiki = Wikipedia(["salut"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url, "https://fr.wikipedia.org/w/index.php?search=salut&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_apostrophe(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant une apostrophe
        """
        my_wiki = Wikipedia(["l'avancement"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url, "https://fr.wikipedia.org/w/index.php?search=l%27avancement&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_apostrophe_2(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant deux apostrophes
        """
        my_wiki = Wikipedia(["c'es't"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url, "https://fr.wikipedia.org/w/index.php?search=c%27es%27t&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_space(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant un espace
        """
        my_wiki = Wikipedia(["bonjour monsieur"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url, "https://fr.wikipedia.org/w/index.php?search=bonjour+monsieur&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_space_2(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant deux espaces
        """
        my_wiki = Wikipedia(["alex est cool"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url, "https://fr.wikipedia.org/w/index.php?search=alex+est+cool&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_plus(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string contenant un plus
        """
        my_wiki = Wikipedia(["a+b"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url, "https://fr.wikipedia.org/w/index.php?search=a%2Bb&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1")

    def test_youtube_url_one_arg_equal(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string contenant un symbole égal
        """
        my_wiki = Wikipedia(["a=b"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url, "https://fr.wikipedia.org/w/index.php?search=a%3Db&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_two_args(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec deux valeurs string
        """
        my_wiki = Wikipedia(["bonjour", "monsieur"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url, "https://fr.wikipedia.org/w/index.php?search=bonjour+monsieur&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_two_args_space(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec deux valeurs string dont une avec un espace
        """
        my_wiki = Wikipedia(["bonjour monsieur", "Obama"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url, "https://fr.wikipedia.org/w/index.php?search=bonjour+monsieur+Obama&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_two_args_plus(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec deux valeurs string dont une avec un symbole
        plus.
        """
        my_wiki = Wikipedia(["salut", "a+b"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url, "https://fr.wikipedia.org/w/index.php?search=salut+a%2Bb&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_bracket_type1(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant un { et un }
        """
        my_wiki = Wikipedia(["alex{tom}"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url, "https://fr.wikipedia.org/w/index.php?search=alex%7Btom%7D&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1")


    def test_wikipedia_url_one_arg_bracket_type2(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant un [ et un ]
        """
        my_wiki = Wikipedia(["alex[tom]"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url, "https://fr.wikipedia.org/w/index.php?search=alex%5Btom%5D&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_star(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant un *
        """
        my_wiki = Wikipedia(["étoile*"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url, "https://fr.wikipedia.org/w/index.php?search=étoile%2A&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_hashtag(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant un #
        """
        my_wiki = Wikipedia(["hash#tag"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url, "https://fr.wikipedia.org/w/index.php?search=hash%23tag&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_no_arg(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments vide
        """
        my_wiki = Wikipedia([])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url, "https://www.wikipedia.org")

    def test_wikipedia_url_one_arg_empty_string(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string vide. create_url interprète ça comme
        une liste vide
        """
        my_wiki = Wikipedia([""])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url, "https://www.wikipedia.org")


if __name__ == '__main__':
    pass

