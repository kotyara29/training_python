

class Animal:
    pass


class Cat(Animal):
    LAPS = 4
    TAIL = True
    def __init__(self, name, age=0):
        self.age = age
        self.sex = 0
        self.weight = 0
        self.name = ""
        self.bread = ""


   # def __new__(cls, *args, **kwargs):
    #    pass


if __name__ == '__main__':
    vasilii = Cat('Vasilii', age=15)
    chernish = Cat('Chernish')
    # chernish.TAIL = "dsds"
    print(vasilii.age)
    print(chernish.TAIL)
    print(f"Cat's name is {chernish.name}")
    print(chernish)
    print(Cat)
