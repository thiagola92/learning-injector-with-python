from injector import inject, Injector, Binder


class FirstClass:
    def __init__(self, number):
        self.example = number


class SecondClass:
    @inject
    def __init__(self, fc: FirstClass):
        self.fc = fc


class ThirdClass:
    @inject
    def __init__(self, sc: SecondClass):
        self.sc = sc


def configure(binder):
    binder.bind(FirstClass, to=FirstClass(100))


injector = Injector(configure)
tc = injector.get(ThirdClass)
print(tc.sc.fc.example)
