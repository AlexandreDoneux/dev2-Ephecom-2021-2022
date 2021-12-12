# python 3.10
# UTF-8
from pip._vendor import requests


class Commande:
    pass

class Itinerary(Commande):
    """
        Itinerary claas who create constructor and methode sho_itinerary who show des informations on the distance and time between two adress
    """
    def __init__(self, origin: str = "", destination: str = ""):
        self._origin = origin
        self._destintion = destination


    def show_itinerary(self):
        """
            Grâce à lapi cette fonction  permet de faire une estimation sur la distance et le temps pour un parcours
            :param
            :return:  bouléen qui permet de savoir si la requette a marché ou pas
        """

        key_api = 'AIzaSyC0kYZMs-Eiosq_lsexBLCKgbkeXWiB95Q'
        base_url = "https://maps.googleapis.com/maps/api/directions/json?"
        origin = input("Adresse de départ: ").replace(' ', '+')
        destination = input("Destination: ").replace(' ', '+')

        complete_url = base_url + "origin=" + origin + "&destination=" + destination + "&key=" + key_api
        try:
            response = requests.get(complete_url)
            response_json = response.json()
            #print(response)
            #print(response_json)
            #print(response_json["routes"])
            lien = "https://www.google.be/maps/dir/" + origin + "+/" + destination
            # print(complete_url)
            stat = 'N OK'
            for status in response_json["geocoded_waypoints"]:
                status_return = status['geocoder_status']
                stat = status_return
            if stat == "OK":
                for i in response_json["routes"]:
                    y = i['legs']
                    #print(y)
                    for j in y:
                        print(f"Vous avez  {j['duration']['text']} pour parcourir {j['distance']['text']}  ")

                print(f"Cliquez pour voir l'itinéraire {lien}")
            else:
                print("Veuillez vérifier l'orthogragphe des adresses ")
        except:
            print("Veuillez verifier votre connexion internet SVP")
        if stat =="OK":
            return True
f = Itinerary()
f.show_itinerary()

# Alfons Moerenhoutstraat 80, Overijse
# Rue Saint Michel 37, Bruxelles
#565 Chemin de Simandres 38200