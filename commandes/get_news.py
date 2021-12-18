# python 3.10
# UTF-8

import requests
from datetime import datetime


class Color:
    """
    Une class qui sers à manipuler l'affichage en gras ou en un autre couleur
    """
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class News:
    def __init__(self, code="be", number=10):

        """
        C'est fonction qui va être appeler par la class News

        :param code str: la personne entrera le code national du pays
        :param number int: la personne entrera un nombre pour avoir le nombre d'article desirer
        """
        self.code = code
        self.number = number

        if type(self.code) != str:
            raise Exception("Le code national doit être une chaine de caractère!")
        if type(self.number) != int:
            raise Exception("Le nombre doit être une chiffre !")
        if self.number < 1:
            raise Exception("Le nombre doit être superieur à 1")

    def news_of_to_day(self):
        """
        Fonction qui servira pour l'affichage d'actualité du jour quelque descriptions

        return: retourne l'actualité avec sa description selon le code national et le nombre d'articles
                qui ont été introduit par l'utilisateur
        """
        code_of_countries = {"ae": "Émirats arabes unis",
                             "ar": "Argentine",
                             "at": "Autriche",
                             "au": "Australie",
                             "be": "Belgique",
                             "bg": "Bulgarie",
                             "br": "Brésil",
                             "ca": "Canada",
                             "ch": "Suisse",
                             "cn": "Chine",
                             "co": "Colombia",
                             "cu": "Cuba",
                             "cz": "Tchéquie",
                             "de": "Allemagne",
                             "fr": "France",
                             "us": "USA",
                             "gb": "Grande Bretagne",
                             "pt": "Portugal"}

        countries = [i + " : " + code_of_countries[i] + "\n" for i in code_of_countries.keys()]
        print("Voici les codes disponibles:\n" + "".join(countries))
        self.code = input("Introduisez le code pays du quel vous voulez voir l'article  :\n")
        while self.code not in code_of_countries:
            self.code = input("Veuillez entrer un code pays valide "
                              + str([i for i in code_of_countries.keys()]) + ": \n")
        state = True
        while state:
            self.number = input("Combien d'articles voulez-vous (max 5) ? :  ")
            if self.number.isdigit() and 0 < int(self.number) <= 5:
                state = False
            else:
                print("ERREUR votre valeur n'est pas valide !")

        api_key = "bb2385450c984f4bacd087cf8df470c3"
        url = "https://newsapi.org/v2/top-headlines?country=" + self.code + "&category=business&apiKey=" + api_key
        news = requests.get(url).json()
        article = news['articles']
        try:
            if self.code in code_of_countries:
                if len(article):
                    if len(article) > int(self.number):
                        for i in range(int(self.number)):
                            channel = article[i]['source']['name']
                            subject = article[i]['title']
                            description = article[i]['description']
                            link = article[i]['url']
                            published_date = article[1]['publishedAt']
                            my_string = str(published_date[:10])
                            hour = str(published_date[11:19])
                            full_time = my_string + ' ' + hour
                            my_date = datetime.strptime(full_time, '%Y-%m-%d %H:%M:%S')

                            print(Color.BOLD, Color.UNDERLINE + "Actualité du jour: " + str(i + 1) + Color.END)
                            print(Color.BOLD, "L'article a été publié par la chaine: ", Color.END, Color.BLUE, channel,
                                  Color.END)
                            print(Color.BOLD, "Le sujet de l'article: ", Color.END, subject)
                            print(Color.BOLD, "Petit resumé du contenu: ", Color.END, description)
                            print(Color.BOLD, "Lien de l'article: ", Color.END, link)
                            print(Color.END, "Date de publication: ", Color.END, my_date.strftime("%A"), my_date.day,
                                  my_date.strftime("%B"), my_date.year, 'at', my_date.strftime("%H") +
                                  ":" + my_date.strftime("%M"), "minutes")
                            print("\n")
                    else:
                        print("le nombre d'articles est introuvable, \n Essayez avec un nombre inferieur !")
            else:
                print("L'indentification ne se trouve pas dans la list")
        except:
            raise Exception("Vous n'avez pas complété le nombre d'article !")


if __name__ == '__main__':
    n1 = News()
    n1.news_of_to_day()
