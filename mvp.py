import requests


def call_help():
    print("Bienvenue dans cette aide du module 'chat multimedia'")
    print("-----------------------------------------------------")
    print("Voici les commandes existantes:")
    print("La commande meteo:\n"
          + "Description: Permet d'avoir des informations sur la météo d'une certaine ville\n"
          + "Utilisation: \meteo nomDeLaVille\n")


def call_weather(request):
    # clé de l'API
    api_key = "923ec08eb99f30d7672f5bc5aa6d2172"
    # url qui va changer dynamiquement
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = (request[1][0].upper()+request[1][1:].lower())
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    # retourne la reponse en objet
    response = requests.get(complete_url)
    x = response.json()
    # si le cod égale 404, la ville n'existe pas
    if x["cod"] != "404":
        # tout la réponse JSON
        y = x["main"]
        # Temperature convertie en celcius
        current_temperature = (y["temp"] - 273.15).__round__(1)
        # stocke l'humidité
        current_humidity = y["humidity"]
        # description du temps
        # weather_description = x["weather"][0]["description"]
        # affichage
        print("Voici les différentes informations pour la météo à "+city_name)
        print("Temperature (en °C): " +
              str(current_temperature) + " °C" +
              "\nHumidité de l'air: " +
              str(current_humidity)+"%")
        # "\Description = " +
        # str(weather_description))
    else:
        print("La ville n'existe pas")


# strip enleve les espaces inutiles à gauche et à droite
my_request = (input("Nom de la requête: ").strip()).split()
if my_request[0][0] == "/":
    if (my_request[0]).lower() == "/meteo":
        # teste si il y a une ville passée
        if len(my_request) == 2:
            call_weather(my_request)
    elif my_request[0].lower() == "/help":
        call_help()
