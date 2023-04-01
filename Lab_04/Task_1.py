import abc
import logging
from abc import ABC, abstractmethod

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG, filename="logs.log", format='%(message)s')
# logger.setLevel(logging.ERROR)

# logging.debug('This is a debug message')
# logging.info('This is an info messageblabla')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


class AbstractCustoms(ABC):
    """

    """
    @abstractmethod
    def enterdata(self):
        pass


class InlandCustoms(AbstractCustoms):
    type = "Inland"

    def __init__(self, name, date):
        self.name = name
        self.date = date

    def enterdata(self):
        self.name = input("Enter the name: ")
        self.date = input("Enter the date: ")

    def __str__(self):
        return f"Customs Type: Inland, Name: {self.name}, Date: {self.date}"


class AirCustoms(AbstractCustoms):
    type = "Air"

    def __init__(self):
        # self.name = name
        # self.date = date

    def enterdata(self, name, date):
        self.name = name
        self.date = date
        self.name = input("Enter the name: ")
        self.date = input("Enter the date: ")

    def __str__(self):
        return f"Customs Type: Air, Name: {self.name}, Date: {self.date}"




new_customs = input("Enter 1 for Air or 2 for Inland Customs: ")
if new_customs == "1":
    new_person = AirCustoms()
#     new_person = AirCustoms(new_name, new_date, new_customs)
else:
    new_person = InlandCustoms()
#     new_person = InlandCustoms(new_name, new_date, new_customs)
# logging.debug(str(new_person).split(', '))
# list_overall.append(new_person)
# print(list_overall)
