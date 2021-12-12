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


if __name__ == '__main__':
    unittest.main()
