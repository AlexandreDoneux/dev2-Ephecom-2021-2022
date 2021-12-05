# coding:utf-8

"""
HAKIZIMANA Aymar Davy
2TL1
Projet Dev2
"""

import requests
from datetime import datetime

class color:
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
    def __init__(self, national_code, number):
        """

        :param national_code str: la personne entrera le code national du pays
        :param number int: la personne entrera un nombre pour avoir le nombre d'article desirer
        """

        self.code = national_code
        self.number = number

    def news_Of_To_Day(self):
        """

        :return:
        """
        api_key = "bb2385450c984f4bacd087cf8df470c3"
        url = "https://newsapi.org/v2/top-headlines?country="+self.code+"&category=business&apiKey=" + api_key
        news = requests.get(url).json()
        article = news['articles']
        print(article[0]['publishedAt'])
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
                    fullTime = my_string + ' ' + hour
                    my_date = datetime.strptime(fullTime, '%Y-%m-%d %H:%M:%S')

                    print(color.BOLD,color.UNDERLINE+"Actualité du jour: "+ str(i+1) +color.END)
                    print(color.BOLD,"L'article a été publié par la chaine: ",color.END,color.BLUE,channel,color.END)
                    print(color.BOLD,"Le sujet de l'article: ",color.END,subject)
                    print(color.BOLD,"Petit resumer du contenu: ",color.END,description)
                    print(color.BOLD,"Fait un clic sur le lien pour avoir toute l'article: ",color.END,link)
                    print(color.END,"Publié: ",color.END, my_date.strftime("%A"),
                      my_date.day, my_date.strftime("%B"),
                      my_date.year, 'at', my_date.strftime("%H") + ":" + my_date.strftime("%M"), "minutes")
                    print("\n")

            else:
                print("Impossible d'avoir le nombre d'article que vous avez demandé")
        else:
            print("L'identification national n'existe pas")

identNational = str(input("Entre le code national du pays :"))
n = int(input("Introduisez le nombre d'article du jour que vous voulez voir :"))

if __name__=='__main__':
    n1 = News(identNational,n)
    n1.news_Of_To_Day()