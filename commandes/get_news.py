"""
HAKIZIMANA Aymar Davy
2TL1
Projet Dev2
"""


import requests

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
    def __init__(self, channel):
        self.channel = channel

    def news_Of_To_Day(self):

        if self.channel == "bbc" or self.channel == "BBC":
            self.channel = self.channel + "-news"
        api_key = "bb2385450c984f4bacd087cf8df470c3"
        url = "https://newsapi.org/v2/top-headlines?sources="+self.channel+"&apiKey=" + api_key
        news = requests.get(url).json()
        article = news['articles']

        for i in range(len(article)):
            channel = article[i]['source']['name']
            subject = article[i]['title']
            description = article[i]['description']
            link = article[i]['url']
            diffusionDate = article[i]['publishedAt']

            print(color.BOLD,color.UNDERLINE+"Those are the news of today: news number:"+ str(i+1) +color.END)
            print(color.BOLD,"L'article a été publié par la chaine: ",color.END,channel)
            print(color.BOLD,"Le sujet de l'article: ",color.END,subject)
            print(color.BOLD,"Petit resumer du contenu: ",color.END,description)
            print(color.BOLD,"Vous pouvez clicker sur le lien ce lien si vous desirez lire toute l'article: ",color.END,link)
            print(color.BOLD,"La date de difussion est :",color.END, diffusionDate)
            print("\n")
n1 = News('CNN')
n1.news_Of_To_Day()

# key api : bb2385450c984f4bacd087cf8df470c3
