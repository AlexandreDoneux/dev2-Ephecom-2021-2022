from datetime import datetime as date


class Date:
    def __init__(self, fr=True, present_day=date.now()):
        """
        Fonction appelée à la création de la date
        :param fr:  un boolean étant à True si on veut la date en français ou False si on la veut en anglais
        :param present_day: contiendra la date à afficher
        """
        if isinstance(fr, bool):
            self.__fr = fr
            self.__day_name = present_day.strftime("%A")
            self.__day_number = present_day.strftime("%d")
            self.__month_name = present_day.strftime("%B")
            self.__year_number = present_day.strftime("%G")
            self.__date_completed = ""
            self.calculate_date()
        else:
            raise TypeError

    def __str__(self):
        """
        Fonction appelée quand on veut afficher la date
        :return: une String contenant une phrase disant la date
        """
        return self.__date_completed

    def calculate_date(self):
        """
        Fonction qui stock une string donnant la date du jour dans self.__date_completed
        """
        if self.__fr:
            self.__day_name = self.__day_name.replace("Monday", "Lundi")
            self.__day_name = self.__day_name.replace("Tuesday", "Mardi")
            self.__day_name = self.__day_name.replace("Wednesday", "Mercredi")
            self.__day_name = self.__day_name.replace("Thursday", "Jeudi")
            self.__day_name = self.__day_name.replace("Friday", "Vendredi")
            self.__day_name = self.__day_name.replace("Saturday", "Samedi")
            self.__day_name = self.__day_name.replace("Sunday", "Dimanche")

            self.__month_name = self.__month_name.replace("January", "Janvier")
            self.__month_name = self.__month_name.replace("February", "Fevrier")
            self.__month_name = self.__month_name.replace("March", "Mars")
            self.__month_name = self.__month_name.replace("April", "Avril")
            self.__month_name = self.__month_name.replace("May", "Mai")
            self.__month_name = self.__month_name.replace("June", "Juin")
            self.__month_name = self.__month_name.replace("July", "Juillet")
            self.__month_name = self.__month_name.replace("August", "Aout")
            self.__month_name = self.__month_name.replace("September", "Septembre")
            self.__month_name = self.__month_name.replace("October", "Octobre")
            self.__month_name = self.__month_name.replace("November", "Novembre")
            self.__month_name = self.__month_name.replace("December", "Decembre")

            self.__date_completed = f"Nous sommes {self.__day_name.lower()} le " \
                                    f"{self.__day_number} {self.__month_name.lower()} {self.__year_number}"

        else:
            self.__date_completed = f"We are {self.__day_name} the {self.__day_number}th" \
                                    f" of {self.__month_name} {self.__year_number}"


"""Examples
date1 = Date()
print(date1)
date2 = Date(False)
print(date2)
"""

"""help_date = "Aide de la commande date\nDescription: commande permettant d'afficher la date au format anglais" \
            " ou français (par défaut, l'affichage est en français)\n" \
            "Utilisation: /date [eng ou fr]\n[]: paramètre optionnel\n"
print(help_date)"""
