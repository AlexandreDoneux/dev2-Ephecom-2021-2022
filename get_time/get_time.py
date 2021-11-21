from datetime import datetime


class Time:
    def __init__(self, fr=True):
        self.__fr = fr
        self.__time_completed = ""
        self.calculate_time()

    def __str__(self):
        return self.__time_completed

    def calculate_time(self):
        """
        Fonction qui stock une string stockant l'heure dans self.__time_completed
        :param: self pour savoir si fr = True ou non
        """
        if self.__fr:
            self.__time_completed = f'Il est {datetime.now().strftime("%H:%M")}'

        else:
            hours = int(datetime.now().strftime("%H"))
            if hours >= 12:
                hours -= 12
                self.__time_completed = f"It's {hours}:{datetime.now().strftime('%M')} PM"
            else:
                self.__time_completed = f"It's {hours}:{datetime.now().strftime('%M')} AM"

"""Examples
time1 = Time()
print(time1)
time2 = Time(False)
print(time2)
"""
