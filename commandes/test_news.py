# python 3.10
# UTF-8
import requests
import unittest
from get_news import News
from get_news import color


class News_test(unittest.TestCase):
    def test_color(self):
        """
        Test pour la class des couleurs pour chaque attribue se trouvant dans la class Color
        :return:Il retourne une phrase ou un mot qui est modifier en gras ou en couleur
        """
        self.assertEqual(color.RED + "Hakizimana" + color.END, "[91mHakizimana[0m")
        self.assertNotEqual(color.RED+"Article"+color.RED, "Article")
        self.assertEqual(color.UNDERLINE+"Article du jour"+color.END,"[4mArticle du jour[0m")


    def test__init__news(self):
        """
        #Test dans l'initialisation de la class News
        :return:Il retourne rien
        """
        n1 = News("be",1)
        self.assertEqual(n1.news_Of_To_Day(), None)

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
        self.assertTrue(News("fr", 12), News("fr",12).number in int)


if __name__ == '__main__':
    News_test.run()
