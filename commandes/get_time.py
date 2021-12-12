# python 3.10
# UTF-8
from datetime import datetime as date


class Time:
    def __init__(self, fr=True, time=date.now()):
        """
        Fonction appelée à la class Time
        :param fr: un boolean étant à True si on veut l'heure en français ou False si on la veut en anglais
        :param time: contiendra l'heure sur laquelle on veut travailler
        """
        if isinstance(fr, bool):
            self.__fr = fr
            self.__time_completed = ""
            self.calculate_time(time)
        else:
            raise TypeError

    def __str__(self):
        """
        Fonction appelée à l'affichage de l'heure
        :return: une String contenant une phrase donnant l'heure
        """
        return self.__time_completed

    def calculate_time(self, time):
        """
        Fonction qui stock une string stockant l'heure dans self.__time_completed
        :param: self pour savoir si fr = True ou non
        """
        if self.__fr:
            self.__time_completed = f'Il est {time.strftime("%H:%M")}'

        else:
            hours = int(time.strftime("%H"))
            if hours >= 12:
                hours -= 12
                self.__time_completed = f"It's {hours}:{time.strftime('%M')} PM"
            else:
                self.__time_completed = f"It's {hours}:{time.strftime('%M')} AM"


""" Examples
time1 = Time()
print(time1)
time2 = Time(False)
print(time2)
"""
