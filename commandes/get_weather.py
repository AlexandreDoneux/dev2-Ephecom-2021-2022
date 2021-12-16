import requests


class Weather:
    def __init__(self, request):
        """
        Fonction appelé à la création d'une meteo
        :param request: String contenant un nom de ville
        """
        self.__request = request

    def show_weather(self):
        """
        Fonction qui affiche la meteo d'une ville ainsi que l'humidité en pourcent
        """
        # clé de l'API
        api_key = "923ec08eb99f30d7672f5bc5aa6d2172"
        # url qui va changer dynamiquement
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = (self.__request[0].upper() + self.__request[1:].lower())
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
            # affichage
            print("Voici les différentes informations pour la météo à " + city_name + ":")
            print(" - Temperature (en °C): " +
                  str(current_temperature) + " °C" +
                  "\n - Humidité de l'air: " +
                  str(current_humidity) + "%")
        else:
            print("La ville n'existe pas")
