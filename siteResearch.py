# python 3.10
# alexandre Doneux
# 14/11/2021

# définition des fonctions liées à la recherche dans d'autres sites
# Deux possibilités: une commande qui analyse et renvoie vers le site particulier
                   # une commande pour chaque site
import webbrowser

def search_site(message):
    """
    Fonction qui a pour but d'analyser le message reçu, de déterminer sur quel site on veut faire la revcherche et 
    effectuer la recherche
    PRE :
    message: String , message sans le "/" et le nom de la commande. On s'attends a ce que le premier mot soit le nom du
                      site (ex: Linedin, youtube, ...). et la suite soit la recherche en elle-même.
    POST:
    Ouvre un onglet dans le navigateur. On effectue directement la recherche dans cet onglet.
    Si message n'est pas un string, renvoie -1.
    Si la commande n'est pas valide (taille, nombre de mots) on renvoie -2 et print un message selon le cas.
    """

    if type(message) != str :
        return(-1)

    if len(message) == 0:
        print("Le message est vide")
        return(-2)

    message = message.split()
    if len(message) < 2:
        print("Le message ne possède pas de recherche")
        return(-2)

    # On détermine pour quel site on veut faire la recherche

    if message[0] == "linkedin":
        if len(message) > 3:
            print("Pour une recherche Linkedin utilisez deux arguments: prénom et nom")
            return(-2)
        # Recherche "Charles Doneux" -> https://fr.linkedin.com/pub/dir?firstName=Charles&lastName=Doneux&trk=public_profile_people-search-bar_search-submit
        webbrowser.open("https://fr.linkedin.com/pub/dir?firstName="+message[1]+"&lastName="+message[2]+
                        "&trk=public_profile_people-search-bar_search-submit")

    if message[0] == "youtube":
        # Recherche "thomas va bien" -> https://www.youtube.com/results?search_query=thomas+va+bien

        urlYoutube = "https://www.youtube.com/results?search_query="
        for i in range(len(message)-1):
            urlYoutube += message[i+1]
            if i != len(message)-2:  # Ajoute un "+" après chaque terme sauf le dernier
                urlYoutube += "+"
            i+=1

        webbrowser.open(urlYoutube)

    if message[0] == "wikipedia":
        # Recherche "repertoire courant" -> https://fr.wikipedia.org/w/index.php?title=Spécial:Recherche&search=repertoire+courant&go=Go&ns0=1

        urlWikipedia = "https://fr.wikipedia.org/w/index.php?title=Spécial:Recherche&search="
        for i in range(len(message)-1):
            urlWikipedia += message[i+1]
            if i != len(message)-2:  # Ajoute un "+" après chaque terme sauf le dernier
                urlWikipedia += "+"
            i+=1
        urlWikipedia += "&go=Go&ns0=1"

        webbrowser.open(urlWikipedia)


# problème Linkedin : Il faut s'inscrire
# problème d'accents dans les url