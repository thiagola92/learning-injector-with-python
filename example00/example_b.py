from injector import inject, Injector


class FirstClass:
    def __init__(self):
        self.example = 100


class SecondClass:
    @inject
    def __init__(self, fc: FirstClass):
        self.fc = fc


injector = Injector()
sc = injector.get(SecondClass)
print(sc.fc.example)
