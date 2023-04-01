import logging
from abc import ABC

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG, filename="logs.log", format='%(message)s')


class AbstractCustoms(ABC):
    type = "Undefined"

    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __str__(self):
        return f"Customs Type: {self.type}, Name: {self.name}, Date: {self.date}"


class InlandCustoms(AbstractCustoms):
    type = "Inland"


class AirCustoms(AbstractCustoms):
    type = "Air"


list_overall, list_inland, list_air = [], [], []


def show_lists():
    select_list = input("Type 1 to see the list of all passengers; "
                        "Type 2 to see the list of aircraft passengers; "
                        "Type 3 to see the list of inland passengers: ")
    if select_list == 1:
        print(list_overall)
    elif select_list == 2:
        print(list_air)
    else:
        print(list_inland)


stop_words = ['STOP', 'END', 'Stop', 'End', 'stop', 'end']
while input("Enter anything to add data on passenger. Enter STOP or END to finish: ") not in stop_words:
    if input("Enter 1 for Air or 2 for Inland Customs: ") == "1":
        new_person = AirCustoms(input("Enter the name: "), input("Enter the date: "))
        logging.debug(str(new_person).split(', '))
        list_overall.append(str(new_person).split(', '))
        list_air.append(str(new_person).split(', '))
    else:
        new_person = InlandCustoms(input("Enter the name: "), input("Enter the date: "))
        logging.debug(str(new_person).split(', '))
        list_overall.append(str(new_person).split(', '))
        list_inland.append(str(new_person).split(', '))

show_lists()
# list_overall.append(new_person)
# print(list_overall)
