# python 3.10
# UTF-8

from commandes import itinerary, get_clean_command, get_date, get_news, get_time, help, show_info, site_search
from commandes import get_weather
from check_connection import check_connection
# Compléter import


def find_command(argument):

    argument[0] = get_clean_command.give_good_command(argument[0])
    if argument[0] == "/info":
        print(show_info.ShowInfo())

    elif argument[0] == '/date':
        if len(argument) == 1:
            print(get_date.Date(True))
        elif get_clean_command.give_good_command(argument[1]) == "eng":
            print(get_date.Date(False))
        elif get_clean_command.give_good_command(argument[1]) == "fr":
            print(get_date.Date(True))
        else:
            print("ERREUR sur les paramètres")
            # détection d'erreur un peu simple. Détection de mauvaise langue? Trop de paramètres?

    elif argument[0] == '/time':
        if len(argument) == 1:
            print(get_time.Time(True))
        elif get_clean_command.give_good_command(argument[1]) == "eng":
            print(get_time.Time(False))
        elif get_clean_command.give_good_command(argument[1]) == "fr":
            print(get_time.Time(True))
        else:
            print("ERREUR sur les paramètres")
            # détection d'erreur un peu simple. Détection de mauvaise langue? Trop de paramètres?

    # besoin connection internet
    elif argument[0] == '/itiner':
        if check_connection():
            api_end_point.Itinerary().show_itinerary()
        else:
            print("Pas de connexion internet.")

    # besoin connection internet
    elif argument[0] == '/youtube':
        if check_connection():
            my_research = site_search.Youtube(argument[1:])
            my_research.create_url_youtube()
            my_research.go_to_site()
        else:
            print("Pas de connexion internet.")
    # besoin connection internet
    elif argument[0] == '/wikipedia':
        if check_connection():
            my_research = site_search.Wikipedia(argument[1:])
            my_research.create_url_wikipedia()
            my_research.go_to_site()
        else:
            print("Pas de connexion internet.")
    # besoin connection internet
    elif argument[0] == '/linkedin':
        if check_connection():
            my_research = site_search.Linkedin(argument[1:])
            my_research.create_url_linkedin()
            my_research.go_to_site()
        else:
            print("Pas de connexion internet.")

    # besoin connection internet
    elif argument[0] == '/meteo':
        if check_connection():
            if len(argument) == 1:
                print("ERREUR pas de ville spécifiée")
            else:
                argument[1] = " ".join(argument[1:])
                get_weather.Weather(argument[1]).show_weather()
        else:
            print("Pas de connexion internet.")

    # besoin connection internet
    elif argument[0] == '/news':
        if check_connection():
            show_news = get_news.News()
            show_news.news_of_to_day()
        else:
            print("Pas de connexion internet")

    elif argument[0] == "/help":
        if len(argument) == 1:
            print(help.Help())
        elif len(argument) == 2:
            argument[1] = get_clean_command.give_good_command(argument[1])
            print(help.Help(argument[1]))
        else:
            print("Erreur. N'indiquez qu'une seule commande.")

    # autre cas -> pas nos commandes
    else:
        pass

if __name__ == "__main__":
    print(check_connection())
        
