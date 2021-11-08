from injector import inject, Injector, Binder

class FirstClass:
    def __init__(self, number):
        self.example = number
    

class SecondClass:
    @inject
    def __init__(self, fc : FirstClass):
        self.fc = fc


def configure(binder):
    binder.bind(FirstClass, to=FirstClass(100))

injector = Injector(configure)
sc = injector.get(SecondClass)
print(sc.fc.example)