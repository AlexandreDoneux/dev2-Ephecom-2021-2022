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


if __name__ == '__main__':
    unittest.main()
