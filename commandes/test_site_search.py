from unittest import TestCase
from site_search import Wikipedia, Linkedin, Youtube

class TestLinkedin(TestCase):
    def test_create_url_linkedin(self):
        link = Linkedin("Thomas", "Delaruelle")
        link.create_url_linkedin()
        self.assertEqual("https://fr.linkedin.com/pub/dir?firstName=Thomas+&lastName=Delaruelle&trk=public_profile_people-search-bar_search-submit",
                         link.url)
        link = Linkedin("Jacques", "De Vannes")
        link.create_url_linkedin()
        self.assertEqual("https://fr.linkedin.com/pub/dir?firstName=Jacques+&lastName=De+Vannes&trk=people-guest_people-search-bar_search-submit",
                         link.url)
        link = Linkedin("Pierre Henry", "James")
        link.create_url_linkedin()
        self.assertEqual("https://fr.linkedin.com/pub/dir?firstName=Pierre+Henry&lastName=James&trk=people-guest_people-search-bar_search-submit",
                         link.url)
        link = Linkedin("Pierre Henry", "James")
        link.create_url_linkedin()
        self.assertEqual("https://fr.linkedin.com/pub/dir?firstName=Pierre+Henry&lastName=James&trk=people-guest_people-search-bar_search-submit",
                         link.url)

# Tests pour linkedin pas complet -> problème d'authentification pour accéder au site.
# Autre problème : différents types de recherche: dans l'url -> "people-guest", "public profile"


class TestWikipedia(TestCase):
    def test_create_url_linkedin(self):
        wiki = Wikipedia("mémoire","partagée")
        wiki.create_url_wikipedia()
        self.assertEqual("https://fr.wikipedia.org/wiki/Mémoire_partagée_(communication_inter-processus)", wiki.url)
        wiki = Wikipedia("Jacques")
        wiki.create_url_wikipedia()
        self.assertEqual("https://fr.wikipedia.org/wiki/Jacques", wiki.url)
        wiki = Wikipedia("spanning", "tree", "protocol")
        wiki.create_url_wikipedia()
        self.assertEqual("https://fr.wikipedia.org/wiki/Spanning_Tree_Protocol", wiki.url)
        wiki = Wikipedia("mémoire partagée")
        wiki.create_url_wikipedia()
        self.assertEqual("test", wiki.url)
        wiki = Wikipedia()
        wiki.create_url_wikipedia()
        self.assertEqual("https://fr.wikipedia.org/w/index.php?search=&title=Spécial:Recherche", wiki.url)
        wiki = Wikipedia("mémoire", "partagée", "charles", "test", "personne", "si", "seulement")
        wiki.create_url_wikipedia()
        self.assertEqual("https://fr.wikipedia.org/w/index.php?search=mémoire+partagée+charles+test+personne+si+seulement&title=Spécial%3ARecherche&ns0=1", wiki.url)

# tests unitaires très complexes. Les urls Wikipedia ne respectent pas la même forme lorsque un article existe ou pas.
# Même si il existe l'url sera parfois modifiée -> redirection
# Cas spécial quand l'url est vide

# rends les tests unitaires très compliqués, voir impossibles


class TestYoutube(TestCase):
    def test_create_url_linkedin(self):
        youtube = Youtube("Salut","c'est","cool")
        youtube.create_url_youtube()
        self.assertEqual("https://www.youtube.com/results?search_query=Salut+c%27est+cool", youtube.url)

# Caractères spéciaux sont parfois traduits dans les url -> chercher module qui transforme
# Sinon vais devoir tester tous les caractères un a un pour faire une liste
