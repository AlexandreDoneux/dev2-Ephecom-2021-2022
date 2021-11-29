import requests
from geopy import Nominatim


class Commande:
    pass


def convert_seconde(total_time: int):
    """

    :param total_time: Reçu de l'API
    :return: retourne le jour, les heures, les minutes et les secondes après calcul
    """
    day = total_time // 86400
    total_time = total_time - 86400 * day
    hour = total_time // 3600
    total_time = total_time - 3600 * hour
    minute = total_time // 60
    seconde = total_time - minute * 60

    return day, hour, minute, seconde


def where_i_am():
    """  function API permettant de trouver sa position actuelle
    :param: aucun paramètre en entrée
    :return:  la latitude et la longitude de sa position actuelle
    """
    response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=03bb117c823f42f68b3c0d70447377af")
    print(response.status_code)
    print(response.json())
    print(response.json()["postal_code"])
    print(response.json()["city"])
    print(response.json()["postal_code"])
    print(response.json()["longitude"])
    print(response.json()["latitude"])

    return response.json()["ip_address"]


def validation_input(message: str):
    """ Fonction qui valide si la saisie est correcte
        :param message: Message affiché à
        :return:  valid_input: l'adresse valide
    """
    valid_input = ""
    valid = False
    while not valid:
        no_valid_input = input(message).replace(' ', '+')
        try:
            locator = Nominatim(user_agent="ephecom")
            location_no_valid_input = locator.geocode(no_valid_input)
            if isinstance(location_no_valid_input.latitude, float) is True:
                valid = True
            valid_input = str(location_no_valid_input.latitude) + ',' + str(location_no_valid_input.longitude)
            print(f'{message} {valid_input}')
        except:
            print(f"L'adresse n'est pas correcte")
    return valid_input


def show_time(return_seconde):
    """

    :param return_seconde: Reçois les minutes
    :return: le  bon affichage
    """
    show = convert_seconde(return_seconde)
    if show[0] == 0:
        if show[1] == 0:
            if show[2] == 0:
                show_str = f'{show[3]} secondes'
            else:
                show_str = f'{show[2]} minute(s)'
        else:
            show_str = f' {show[1]} heure(s){show[2]} minute(s)'
    else:
        show_str = f'{show[0]} jour(s) {show[1]} heure(s) {show[2]} minute(s)'
    return show_str


def show_distance(distance: float):
    """ Fonction qui affiche la distance en Km ou en m
    :param distance:
    :return: message; qui affiche la distance en Km ou m
    """
    if distance > 1000:
        message = f'{round(distance / 1000, 2)} Km'
    else:
        message = f'{distance} m'
    return message


class Itinerary(Commande):
    def __init__(self, departure: str = "", endpoint: str = "", mode_driving='driving'):
        self._departure = departure
        self._endpoint = endpoint
        self._mode_driving = mode_driving


    def show_itinerary(self):
        key_api = '8254223a3c17790d72957eb7c831419d'
        base_url = "https://maps.open-street.com/api/route/?"
        departure = validation_input("Adresse de départ: ")

        endpoint = validation_input(" Adresse de destination: ")


        """
            :param self: Aucune valeur en entrée 
            :return: Aucune valeur de retour
            """
        complete_url = base_url + "origin=" + departure + "&destination=" + endpoint + "&mode=" + self._mode_driving+ "&key=" + key_api

        response = requests.get(complete_url)
        x = response.json()
        #print(x)

        # si le statut est égale 404, la requête a été bien exécutée

        if x["status"] == 'OK':
            depart = departure.replace(' ', '+')
            destination = endpoint.replace(' ', '+')
            lien = "https://www.google.be/maps/dir/" + depart + "+/" + destination
            print(lien)
            print(
                f' Estimation distance à parcourir {show_distance(x["total_distance"])} dans  {show_time(x["total_time"])}')

        else:
            print("Erreur serveur; veuiller recommencer SVP")


Itineraire = Itinerary()
Itineraire.show_itinerary()


