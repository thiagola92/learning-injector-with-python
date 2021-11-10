from injector import inject, Injector, Binder


class FirstClass:
    def __init__(self, number):
        self.example = number


class SecondClass:
    @inject
    def __init__(self, fc: FirstClass):
        self.fc = fc


fc = FirstClass(100)
sc = SecondClass(fc)
print(sc.fc.example)
