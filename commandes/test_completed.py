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
from site_search import Youtube, Linkedin, Wikipedia, no_blank_string_in_list, percent_encoding_url


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
class ColorTest(unittest.TestCase):
    def test_Color(self):
        """
        Test pour la class des couleurs pour chaque attribue se trouvant dans la class Color
        :return:Il retourne une phrase ou un mot qui est modifier en gras ou en couleur
        """
        self.assertEqual(Color.RED + "Hakizimana" + Color.END, "[91mHakizimana[0m")
        self.assertEqual(Color.UNDERLINE + "Article du jour" + Color.END, "[4mArticle du jour[0m")

    def test_notEqual_color(self):
        """
        #Il va verifier "font-color" de la phrase
        """
        self.assertNotEqual(Color.RED + "Article" + Color.RED, "Article")


class NewsTest(unittest.TestCase):
    def test__init__news(self):
        """
        #Test dans l'initialisation de la class News
        :return:Il retourne rien
        """
        n1 = News("be", 1)
        self.assertEqual(News("be", 1).code, "be", "affiche le code du pays")
        self.assertEqual(News("fr", 2).number, 2, "affiche 2 articles demandé")

    def test_codeNational_caracter(self):
        """
        #Il va verifier l'affichage dans la class avec un retour d'une chaine de caractère
        :return:
        """
        self.assertRaises(Exception, "Le code national doit être une chaine de caractère!")

    def test_number_news(self):
        """
        #Il va verifier si le parametre nombre est un chiffre
        """
        self.assertRaises(Exception, "Le nombre doit être une chiffre !")


class HelpTest(unittest.TestCase):
    def test_help_all(self):
        result = "/help [command]      []: paramètre optionnel\nCommande permettant d'afficher les aides des " \
                 "différentes commandes. 'command' représente la commande pour laquelle vous voulez de l'aide. Sans " \
                 "commande spécifié /help renvoie les aides concernant toutes les commandes.\n\n/weather {ville} " \
                 "\nCommande affichant les informations météorologiques de la ville spécifiée. Elle affiche la " \
                 "temperature et l'humidité de l'air.\n\n/news\nPermets à l'utilisateur une recherche sur les articles " \
                 "du jour selon le pays disponible où il veut \nLes pays disponibles sont : [ae: Émirats arabes unis," \
                 " ar: Argentine, at: Autriche, au: Australie, be: Belgique, bg: Bulgarie, br: Brésil, ca: Canada, " \
                 "ch: Suisse, cn: Chine, co: Colombia, cu: Cuba, cz: Tchéquie, de: Allemagne, fr: France, us: USA, " \
                 "gb: Grande Bretagne, pt: Portugal]\n\n/itiner\nPermet de trouver son trajet en faisant l'estimation " \
                 "du temps et de la distance \nL'utilisateur est invité à insérer son adresse de départ ainsi que son" \
                 " adresse de destination.\n\n/linkedin [*research]      []: paramètre optionnel\nCommande permettant " \
                 "l'ouverture et une recherche sur linkedin. research est la recherche, la phrase que vous voulez " \
                 "rechercher. \nSans paramètres de recherche spécifique linkedin est ouvert à sa page d'acceuil.\n\n" \
                 "/youtube [*research]      []: paramètre optionnel\nCommande permettant l'ouverture et une recherche" \
                 " sur youtube. research est la recherche, la phrase que vous voulez rechercher. \nSans paramètres de" \
                 " recherche spécifique youtube est ouvert à sa page d'acceuil.\n\n/wikipedia [*research]      []: " \
                 "paramètre optionnel\nCommande permettant l'ouverture et une recherche sur wikipedia. research est " \
                 "la recherche, la phrase que vous voulez rechercher. \nSans paramètres de recherche spécifique " \
                 "wikipedia est ouvert à sa page d'acceuil.\n\n/info\nCommande permettant d'afficher des informations " \
                 "sur le module de chatbot multimédia.\n\n/time [eng ou fr]      []: paramètre optionnel\nCommande " \
                 "permettant d'afficher l'heure au format anglais ou français (par défaut, l'affichage est en " \
                 "français)\n\n/date [eng/fr]      []: paramètre optionnel\nCommande permettant d'afficher la date au" \
                 " format anglais ou français (par défaut, l'affichage est en français)\n\n"

        self.assertEqual(result, str(Help()))

    def test_help_date(self):
        """
        teste les string qui sera renvoyé lors d'un print d'un objet Help avec une commande qui existe: date
        """
        result = "/date [eng/fr]      []: paramètre optionnel\nCommande permettant d'afficher la date au format " \
                 "anglais ou français (par défaut, l'affichage est en français)\n"
        self.assertEqual(result, str(Help("date")))

    def test_help_itiner(self):
        """
        teste les string qui sera renvoyé lors d'un print d'un objet Help avec une commande qui existe: itiner
        """
        result = "/itiner\nPermet de trouver son trajet en faisant l'estimation du temps et de la distance \n" \
                 "L'utilisateur est invité à insérer son adresse de départ ainsi que son adresse de destination.\n"
        self.assertEqual(result, str(Help("itiner")))

    def test_help_youtube(self):
        """
        teste les string qui sera renvoyé lors d'un print d'un objet Help avec une commande qui existe: youtube
        """
        result = "/youtube [*research]      []: paramètre optionnel\nCommande permettant l'ouverture et une " \
                 "recherche sur youtube. research est la recherche, la phrase que vous voulez rechercher. \nSans " \
                 "paramètres de recherche spécifique youtube est ouvert à sa page d'acceuil.\n"
        self.assertEqual(result, str(Help("youtube")))

    def test_help_wikipedia(self):
        """
        teste les string qui sera renvoyé lors d'un print d'un objet Help avec une commande qui existe: wikipedia
        """
        result = "/wikipedia [*research]      []: paramètre optionnel\nCommande permettant l'ouverture et une " \
                 "recherche sur wikipedia. research est la recherche, la phrase que vous voulez rechercher. \nSans " \
                 "paramètres de recherche spécifique wikipedia est ouvert à sa page d'acceuil.\n"
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
        self.assertEqual(my_wiki.url,
                         "https://fr.wikipedia.org/w/index.php?search=salut&title=Spécial:Recherche&profile="
                         "advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_apostrophe(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant une apostrophe
        """
        my_wiki = Wikipedia(["l'avancement"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url,
                         "https://fr.wikipedia.org/w/index.php?search=l%27avancement&title=Spécial:Recherche&profile="
                         "advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_apostrophe_2(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant deux apostrophes
        """
        my_wiki = Wikipedia(["c'es't"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url,
                         "https://fr.wikipedia.org/w/index.php?search=c%27es%27t&title=Spécial:Recherche&profile="
                         "advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_space(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant un espace
        """
        my_wiki = Wikipedia(["bonjour monsieur"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url,
                         "https://fr.wikipedia.org/w/index.php?search=bonjour+monsieur&title=Spécial:Recherche&profile="
                         "advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_space_2(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant deux espaces
        """
        my_wiki = Wikipedia(["alex est cool"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url,
                         "https://fr.wikipedia.org/w/index.php?search=alex+est+cool&title=Spécial:Recherche&profile="
                         "advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_plus(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string contenant un plus
        """
        my_wiki = Wikipedia(["a+b"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url,
                         "https://fr.wikipedia.org/w/index.php?search=a%2Bb&title=Spécial:Recherche&profile="
                         "advanced&fulltext=1&ns0=1")

    def test_youtube_url_one_arg_equal(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string contenant un symbole égal
        """
        my_wiki = Wikipedia(["a=b"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url,
                         "https://fr.wikipedia.org/w/index.php?search=a%3Db&title=Spécial:Recherche&profile="
                         "advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_two_args(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec deux valeurs string
        """
        my_wiki = Wikipedia(["bonjour", "monsieur"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url,
                         "https://fr.wikipedia.org/w/index.php?search=bonjour+monsieur&title=Spécial:Recherche&profile="
                         "advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_two_args_space(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec deux valeurs string dont une avec un espace
        """
        my_wiki = Wikipedia(["bonjour monsieur", "Obama"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url,
                         "https://fr.wikipedia.org/w/index.php?search=bonjour+monsieur+Obama&title=Spécial:Recherche"
                         "&profile=advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_two_args_plus(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec deux valeurs string dont une avec un symbole
        plus.
        """
        my_wiki = Wikipedia(["salut", "a+b"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url,
                         "https://fr.wikipedia.org/w/index.php?search=salut+a%2Bb&title=Spécial:Recherche&profile="
                         "advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_bracket_type1(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant un { et un }
        """
        my_wiki = Wikipedia(["alex{tom}"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url,
                         "https://fr.wikipedia.org/w/index.php?search=alex%7Btom%7D&title=Spécial:Recherche&profile="
                         "advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_bracket_type2(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant un [ et un ]
        """
        my_wiki = Wikipedia(["alex[tom]"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url,
                         "https://fr.wikipedia.org/w/index.php?search=alex%5Btom%5D&title=Spécial:Recherche&profile="
                         "advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_star(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant un *
        """
        my_wiki = Wikipedia(["étoile*"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url,
                         "https://fr.wikipedia.org/w/index.php?search=étoile%2A&title=Spécial:Recherche&profile="
                         "advanced&fulltext=1&ns0=1")

    def test_wikipedia_url_one_arg_hashtag(self):
        """
        teste l'url générée lorsqu'on utilise une liste arguments avec un string comportant un #
        """
        my_wiki = Wikipedia(["hash#tag"])
        my_wiki.create_url_wikipedia()
        self.assertEqual(my_wiki.url,
                         "https://fr.wikipedia.org/w/index.php?search=hash%23tag&title=Spécial:Recherche&profile="
                         "advanced&fulltext=1&ns0=1")

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


class PercentEncodingUrlTest(unittest.TestCase):
    def test_percent_encoding_all(self):
        """
        test la conversion de caractères spéciaux pour url. On test ici tous les types à la fois
        """
        self.assertEqual(percent_encoding_url("[]{}*#@:=+/?<>$&%!,;()"),
                         "%5B%5D%7B%7D%2A%23%40%3A%3D%2B%2F%3F%3C%3E%24%26%25%21%2C%3B%28%29")
        # possible de faire une vérification sur " et ' ?

    def test_percent_encoding_all_spaces(self):
        """
        test la conversion de caractères spéciaux pour url. On test ici tous les types à la fois et on a des espaces
         dans la string
        """
        self.assertEqual(percent_encoding_url("[]{} *#@:=+/ ?<>$&%!, ;()"),
                         "%5B%5D%7B%7D %2A%23%40%3A%3D%2B%2F %3F%3C%3E%24%26%25%21%2C %3B%28%29")

    def test_percent_encoding_empty(self):
        """
        test la conversion de caractères spéciaux pour url vide.
        """
        self.assertEqual(percent_encoding_url(""), "")

    def test_percent_encoding_nothing(self):
        """
        test la conversion de caractères spéciaux pour url vide.
        """
        self.assertEqual(percent_encoding_url(), "")

    def test_percent_encoding_int(self):
        """
        test la conversion de caractères spéciaux pour url qui est un nombre entier.
        La fonction testée doit renvoyer False.
        """
        self.assertEqual(percent_encoding_url(67), False)

    def test_percent_encoding_float(self):
        """
        test la conversion de caractères spéciaux pour url qui est un nombre décimal.
        La fonction testée doit renvoyer False.
        """
        self.assertEqual(percent_encoding_url(6.666), False)

    def test_percent_encoding_object(self):
        """
        test la conversion de caractères spéciaux pour url qi est un objet.
        La fonction testée doit renvoyer False.
        """
        my_object = Wikipedia(["alex"])
        self.assertEqual(percent_encoding_url(my_object), False)

    def test_percent_encoding_normal_string(self):
        """
        test la conversion de caractères spéciaux pour url qui ne contient aucun caractère spécial
        """
        self.assertEqual(percent_encoding_url("Comment"), "Comment")

    def test_percent_encoding_space(self):
        """
        test la conversion de caractères spéciaux pour url avec espaces qui ne contient aucun caractère spécial
        """
        self.assertEqual(percent_encoding_url("Comment est-ce possible?"), "Comment est-ce possible%3F")


class NoBlankStringTest(unittest.TestCase):
    def test_no_blank_in_string_in_list(self):
        """
        Teste la division d'un élément d'une liste en plusieurs
        """
        my_list = ["salut", "comment ça", "va?"]
        self.assertEqual(no_blank_string_in_list(my_list), ["salut", "comment", "ça", "va?"])
        my_list = ["salut", "comment ça va", "Charles?"]
        self.assertEqual(no_blank_string_in_list(my_list), ["salut", "comment", "ça", "va", "Charles?"])
        my_list = ["salut poto,", "comment ça", "va?"]
        self.assertEqual(no_blank_string_in_list(my_list), ["salut", "poto,", "comment", "ça", "va?"])

    def test_no_blank_in_string_in_list_multiple(self):
        """
        Teste la division d'un élément d'une liste en plusieurs
        """
        my_list = ["salut mon cher", "comment ça", "va?"]
        self.assertEqual(no_blank_string_in_list(my_list), ["salut", "mon", "cher", "comment", "ça", "va?"])
        my_list = ["salut", "comment ça va", "Charles mon ami?"]
        self.assertEqual(no_blank_string_in_list(my_list), ["salut", "comment", "ça", "va", "Charles", "mon", "ami?"])
        my_list = ["a a a a a a a a", "b bb b"]
        self.assertEqual(no_blank_string_in_list(my_list), ["a", "a", "a", "a", "a", "a", "a", "a", "b", "bb", "b"])

    def test_no_blank_in_string_in_list_empty_strings(self):
        """
        Teste la division d'un élément d'une liste ayant la forme d'un string vide
        """
        my_list = ["", "", ""]
        self.assertEqual(no_blank_string_in_list(my_list), [])
        my_list = ["", "", "", "", "", "", "", ""]
        self.assertEqual(no_blank_string_in_list(my_list), [])

    def test_no_blank_in_string_in_list_empty(self):
        """
        Teste la division d'une liste vide
        """
        my_list = []
        self.assertEqual(no_blank_string_in_list(my_list), [])

    def test_no_blank_in_string_in_list_int(self):
        """
        Teste la division d'une liste contenant des int. Ils seront transformés en string
        """
        my_list = [33, 44, 765]
        self.assertEqual(no_blank_string_in_list(my_list), ["33", "44", "765"])
        my_list = [334, 44, 7, 3, 98, 3]
        self.assertEqual(no_blank_string_in_list(my_list), ["334", "44", "7", "3", "98", "3"])

    def test_no_blank_in_string_in_list_float(self):
        """
        Teste la division d'une liste contenant des float. Ils seront transformés en string
        """
        my_list = [33.33, 44.44, 765.1]
        self.assertEqual(no_blank_string_in_list(my_list), ["33.33", "44.44", "765.1"])
        my_list = [334.2, 44.3, 7.1, 3.1, 98.09, 3.22]
        self.assertEqual(no_blank_string_in_list(my_list), ["334.2", "44.3", "7.1", "3.1", "98.09", "3.22"])

    def test_no_blank_in_string_in_list_obj(self):
        """
        Teste la division d'une liste contenant des objets. -> Doit renvoyer False
        """
        my_object1 = Wikipedia(["tom"])
        my_object2 = Wikipedia(["jedusor"])
        self.assertEqual(no_blank_string_in_list([my_object1, my_object2]), False)

    def test_no_blank_in_string_in_list_obj_arg(self):
        """
        Teste quand l'argument est un objet
        """
        my_object = Wikipedia(["alex"])
        self.assertEqual(no_blank_string_in_list(my_object), False)

    def test_no_blank_in_string_in_list_dict(self):
        """
        Teste quand la liste possède des dictionnaires -> Doit renvoyer False
        """
        my_dict1 = {"a": "aaaa"}
        my_dict2 = {"b": "bbb"}
        self.assertEqual(no_blank_string_in_list([my_dict1, my_dict2]), False)

    def test_no_blank_in_string_in_list_dict_arg(self):
        """
        Teste quand l'argument est un dictionnaire
        """
        my_dict = {"a": "aaa", "b": "bbb"}
        self.assertEqual(no_blank_string_in_list(my_dict), False)

    def test_no_blank_in_string_in_list_set_arg(self):
        """
        Teste quand l'argument est un set
        """
        self.assertEqual(no_blank_string_in_list({1, 2, 2, 4, 5}), False)

    def test_no_blank_in_string_in_list_set(self):
        """
        Teste quand la liste d'arguments possèdent des set -> Doit renvoyer False
        """
        self.assertEqual(no_blank_string_in_list([{1, 2, 2, 4, 5}, {1, 1, 1}]), False)

    def test_no_blank_in_string_in_list_bool_arg(self):
        """
        Teste quand l'argument est un booleen
        """
        self.assertEqual(no_blank_string_in_list(True), False)
        self.assertEqual(no_blank_string_in_list(False), False)

    def test_no_blank_in_string_in_list_bool(self):
        """
        Teste quand la liste possède des booléens.
        """
        self.assertEqual(no_blank_string_in_list([True, False]), ["True", "False"])

    def test_no_blank_in_string_in_list_Tuple_arg(self):
        """
        Teste quand l'argument est un tuple.
        """
        self.assertEqual(no_blank_string_in_list((1, 2, 3)), False)

    def test_no_blank_in_string_in_list_Tuple(self):
        """
        Teste quand la liste possède des tuples. -> Doit renvoyer False
        """
        my_tuple1 = (1, 2, 3)
        my_tuple2 = (4, 4, 4)
        self.assertEqual(no_blank_string_in_list([my_tuple1, my_tuple2]), False)


if __name__ == '__main__':
    pass
