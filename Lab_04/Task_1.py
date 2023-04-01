import logging
from abc import ABC

logger = logging.getLogger('main_log')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
fhandlermain = logging.FileHandler('logs.log')
fhandlermain.setFormatter(formatter)
logger.addHandler(fhandlermain)
# logging.basicConfig(level=logging.DEBUG, filename="logs.log", format='%(message)s')
backup_logger = logging.getLogger('backup_log')
backup_logger.setLevel(logging.DEBUG)
backup_formatter = logging.Formatter('%(message)s')
fhandlerbackup = logging.FileHandler("/Users/darkhan/Desktop/Python_code/training_python/training_python/Backup_log_for_Lab04/backuplog.log")
fhandlerbackup.setFormatter(backup_formatter)
backup_logger.addHandler(fhandlerbackup)
# logging.basicConfig(level=logging.DEBUG, filename="/Users/darkhan/Desktop/Python_code/training_python/training_python/Backup_log_for_Lab04/standbylog.log", format="%(message)s")


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
    if select_list == "1":
        print(list_overall)
    elif select_list == "2":
        print(list_air)
    else:
        print(list_inland)
    if_repeat = input("Do you want to see another list? Y/N: ")
    if if_repeat.lower() == "y":
        show_lists()


stop_words = ['STOP', 'END', 'Stop', 'End', 'stop', 'end']
while input("Enter anything to add data on passenger. Enter STOP or END to finish: ") not in stop_words:
    if input("Enter 1 for Air or 2 for Inland Customs: ") == "1":
        new_person = AirCustoms(input("Enter the name: "), input("Enter the date: "))
        logger.debug(str(new_person).split(', '))
        backup_logger.debug(str(new_person).split(', '))
        list_overall.append(str(new_person).split(', '))
        list_air.append(str(new_person).split(', '))
    else:
        new_person = InlandCustoms(input("Enter the name: "), input("Enter the date: "))
        logger.debug(str(new_person).split(', '))
        backup_logger.debug(str(new_person).split(', '))
        list_overall.append(str(new_person).split(', '))
        list_inland.append(str(new_person).split(', '))

show_lists()
# list_overall.append(new_person)
# print(list_overall)
