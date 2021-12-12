# python 3.10
# UTF-8

from commandes import api_end_point, get_clean_command, get_date, get_news, get_time, help, show_info, site_search
from commandes import get_weather
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

    elif argument[0] == '/time':
        if len(argument) == 1:
            print(get_time.Time(True))
        elif get_clean_command.give_good_command(argument[1]) == "eng":
            print(get_time.Time(False))
        elif get_clean_command.give_good_command(argument[1]) == "fr":
            print(get_time.Time(True))
        else:
            print("ERREUR sur les paramètres")

    elif argument[0] == '/itiner':
        api_end_point.Itinerary().show_itinerary()

    elif argument[0] == '/youtube':
        my_research = site_search.Youtube(argument[1:])
        my_research.create_url_youtube()
        my_research.go_to_site()
    elif argument[0] == '/wikipedia':
        my_research = site_search.Wikipedia(argument[1:])
        my_research.create_url_wikipedia()
        my_research.go_to_site()
    elif argument[0] == '/linkedin':
        my_research = site_search.Linkedin(argument[1:])
        my_research.create_url_linkedin()
        my_research.go_to_site()
    elif argument[0] == '/meteo':
        if len(argument) == 1:
            print("ERREUR pas de ville spécifiée")
        else:
            get_weather.Weather(argument[1]).show_weather()

    elif argument[0] == '/news':
        show_news = get_news.News()
        show_news.news_Of_To_Day()

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
        
