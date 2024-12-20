from enum import Enum, auto
from abc import ABC


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious')


class Cofee(HotDrink):
    def consume(self):
        print('This cofee is delicious')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Put in tea bag, boil water, pour {amount}ml, enjoy!")
        return Tea()


class CofeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Grind some beans, boil water, pour {amount}ml, enjoy!")
        return Cofee()


def make_drink(dtype):
    if dtype == 'tea':
        return TeaFactory().prepare(200)
    elif dtype == 'cofee':
        return CofeeFactory().prepare(200)
    else:
        return None


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFEE = auto()
        TEA = auto()

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
        print('Available drinks: ')
        for f in self.factories:
            print(f[0])

        s = input(f"Please pick drink(0-{len(self.factories)-1}): ")
        idx = int(s)
        s = input(f"Specify amount: ")
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


if __name__ == '__main__':
    hdm = HotDrinkMachine()
    hdm.make_drink()
