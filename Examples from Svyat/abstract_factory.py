from abc import ABC, abstractmethod
from enum import Enum, auto


class HotDrink(ABC):
    @abstractmethod
    def consume(self):
        pass

class Cacao(HotDrink):
    def consume(self):
        print("MMMMMM cacao, I like it")

class Tea(HotDrink):
    def consume(self):
        print('This tea is nice but I\'d prefer it with milk')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass

class CacaoFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Crate greates cacao in the world. About {amount}ml.")
        return Cacao()

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()


class HotDrinkMachine:
    class AvailableDrink(Enum):  # violates OCP
        COFFEE = auto()
        TEA = auto()
        CACAO = auto

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks:')
        for idx in range(len(self.factories)):
            print(f"{idx} {self.factories[idx][0]}")

        s = input(f'Please pick drink (0-{len(self.factories) - 1}): ')
        idx = int(s)
        s = input(f'Specify amount: ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


def make_drink(drink_type):
    if drink_type == 'tea':
        return TeaFactory().prepare(200)
    elif drink_type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None


if __name__ == '__main__':
    # entry = input('What kind of drink would you like?')
    # drink = make_drink(entry)
    # drink.consume()

    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()
