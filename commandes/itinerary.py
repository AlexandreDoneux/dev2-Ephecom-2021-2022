# python 3.10
# UTF-8
from pip._vendor import requests


class Commande:
    pass


class Itinerary(Commande):
    """
    La classe itinéraire crée un constructeur et une méthode qui permet d'afficher la distance et une estimation de
    temps pour un trajet
    """

    def __init__(self, origin: str = "", destination: str = ""):
        self._origin = origin
        self._destination = destination

    def show_itinerary(self):
        """
            Grâce à l'api cette fonction  permet de faire une estimation sur la distance et le temps pour un parcours
            :return:  boulean qui permet de savoir si la requette a marché ou pas
        """

        key_api = 'AIzaSyC0kYZMs-Eiosq_lsexBLCKgbkeXWiB95Q'
        base_url = "https://maps.googleapis.com/maps/api/directions/json?"
        if self._origin == '' and self._destination == '':
            origin = input("Adresse de départ: ").replace(' ', '+')
            destination = input("Destination: ").replace(' ', '+')
        else:
            origin = self._origin
            destination = self._destination
        complete_url = base_url + "origin=" + origin + "&destination=" + destination + "&key=" + key_api
        status = 'NOT_FOUNDS' or 'ZERO_RESULTS'
        try:
            response = requests.get(complete_url)
            response_json = response.json()
            # print(response)
            status = response_json["status"]
            if status != "OK":
                print("Veuillez vérifier l'orthogragphe des adresses ")
            else:
                # print(response_json["routes"])
                lien = "https://www.google.be/maps/dir/" + origin + "+/" + destination
                for i in response_json["routes"]:
                    y = i['legs']
                    for j in y:
                        print(f"Vous avez  {j['duration']['text']} pour parcourir {j['distance']['text']}  ")
                        print(f"Cliquez pour voir l'itinéraire {lien}")
        except:
            print("Veuillez verifier votre connexion internet SVP")
        return status

# f = Itinerary()
# f.show_itinerary()

# Alfons Moerenhoutstraat 80, Overijse
# Rue Saint Michel 37, Bruxelles
# 565 Chemin de Simandres 38200
